from flask import Flask, jsonify
from faker import Faker
import random

app = Flask(__name__)
fake = Faker()

# List of cyberpunk-themed jobs and nicknames
jobs = [
    "Street Samurai", "Netrunner", "Fixer", "Techie", "Media", "Solo", "Nomad", "Cop", "Corporate", "Rockerboy",
    "Medtech", "Investigator", "Hacker", "Ripperdoc", "Smuggler", "Engineer", "Data Broker", "Cyber-Detective",
    "Enforcer", "Bounty Hunter", "Mechanic", "Drone Operator", "Biotechnician", "Cybersecurity Specialist",
    "AI Programmer", "Augmentation Specialist", "Genetic Engineer"
]

nicknames = [
    "Ghost", "Shadow", "Razor", "Blaze", "Viper", "Sphinx", "Reaper", "Cipher", "Phantom", "Neon", "Blitz", "Chrome",
    "Nexus", "Holo", "Glitch", "Onyx", "Pulse", "Matrix", "Null", "Byte", "Slash", "Cobalt", "Venom", "Wraith",
    "Ember", "Rift", "Storm", "Havoc", "Zen", "Apex", "Reactor", "Drifter", "Vector", "Echo", "Cipher", "Talon",
    "Vortex"
]
# Generate random cyberpunk data on startup
cyberpunk_data = {
    "name": fake.name(),
    "job": random.choice(jobs),
    "nickname": random.choice(nicknames),
    "net_worth": f"{random.randint(1000, 1000000)} Eurodollars"
}

@app.route('/', methods=['GET'])
def get_cyberpunk_data():
    return jsonify(cyberpunk_data)

if __name__ == '__main__':
    app.run(debug=True)
