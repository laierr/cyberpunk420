from flask import Flask, jsonify
import etcd3
import os
import threading
import random
import time
from faker import Faker

app = Flask(__name__)
client = etcd3.client(host=os.getenv('ETCD_HOST', 'localhost'), port=2379)

# Expanded list of cyberpunk-themed jobs and nicknames
jobs = [
    "Street Samurai", "Netrunner", "Fixer", "Techie", "Media", "Solo", "Nomad", "Cop", "Corporate", "Rockerboy",
    "Medtech", "Investigator", "Hacker", "Ripperdoc", "Smuggler", "Engineer", "Data Broker", "Cyber-Detective",
    "Enforcer", "Bounty Hunter", "Mechanic", "Drone Operator", "Biotechnician", "Cybersecurity Specialist",
    "AI Programmer", "Augmentation Specialist", "Genetic Engineer"
]

nicknames = [
    "Ghost", "Shadow", "Razor", "Blaze", "Viper", "Sphinx", "Reaper", "Cipher", "Phantom", "Neon", "Blitz", "Chrome",
    "Nexus", "Holo", "Glitch", "Onyx", "Pulse", "Matrix", "Null", "Byte", "Slash", "Cobalt", "Venom", "Wraith",
    "Ember", "Rift", "Storm", "Havoc", "Zen", "Apex", "Reactor", "Drifter", "Vector", "Echo", "Talon", "Vortex"
]

# Generate random cyberpunk data on startup
fake = Faker()
cyberpunk_data = {
    "name": fake.name(),
    "job": random.choice(jobs),
    "nickname": random.choice(nicknames),
    "net_worth": f"{random.randint(1000, 1000000)} Eurodollars"
}

# Initialize instance ID and keys
instance_id = cyberpunk_data["nickname"]
leader_key = '/leader'
chatlog_key = '/chatlog'

def become_leader():
    while True:
        # Try to become the leader
        is_leader, _ = client.transaction(
            compare=[
                client.transactions.create(leader_key) == 0
            ],
            success=[
                client.transactions.put(leader_key, instance_id, lease=client.lease(10))
            ],
            failure=[]
        )
        if is_leader:
            break
        time.sleep(1)

def leader_work():
    while True:
        # Leader work: Deliver message
        client.put(chatlog_key, f"We are going to plan a heist [Leader: {instance_id}]")
        time.sleep(10)

def follower_work():
    while True:
        # Follower work: Send agreement
        _, chatlog = client.get(chatlog_key)
        if chatlog:
            client.put(chatlog_key, f"Yes, let's do that [Follower: {instance_id}]")
        time.sleep(10)

def work():
    become_leader()
    if instance_id in nicknames[:5]:  # Assuming first 5 nicknames are participants
        leader_work()
    else:
        follower_work()

@app.route('/start', methods=['GET'])
def start():
    return jsonify({"status": "started", "instance_id": instance_id})

@app.route('/chatlog', methods=['GET'])
def get_chatlog():
    _, chatlog = client.get(chatlog_key)
    if chatlog:
        return jsonify({"chatlog": chatlog.decode('utf-8')})
    return jsonify({"chatlog": "No messages yet"})

if __name__ == '__main__':
    threading.Thread(target=work).start()
    app.run(host='0.0.0.0', port=5000)
