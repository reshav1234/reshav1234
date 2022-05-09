# Blue print for first block chain
import hashlib
import json 
from textwrap import dedent
from time import time     
from uuid import uuid4

from flask import Flask 



class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transaction = []

        # Creating a genesis block
        self.new_block(previous_hash = 1, proof = 1000)


    def new_block(self, proof, previous_has):
        # Creates a new block and add it to the chain
        block = {
            'index' : len(self.chain) + 1,
            'timestamp' : time(),
            'transaction' : self.current_transaction,
            'proof' : proof,
            'previous_hash' : self.hash(self.chain[-1]),
        }

        # Reset the current list of transaction
        self.current_transaction = []
        self.chain.append(block)
        return block 

    def new_transaction(self, sender, recipient, amount):
        # adds a transaction to the list of trasnaction
        self.current_transaction.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })
        return self.last_block['index'] + 1
   
    @staticmethod
    def hash(block):
        
        # Hashes a block
        block_string = json.dump(block, sort_keys = True).encode() 
        """ Storing in dictionary in order:or we will have inconsistent hashes """

        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self):
        # Returns last block in the chain
        return self.chain[-1]


    # Proof of work
    def proof_of_work(self, last_proof):
        """
        simple proof of work algorithm 
        - Find the number p' such that hash(pp') contains leading 4 zeros, where p is previous p'
        - p' is previous proof and p is new proof 
        """
        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1
        return proof 

    @staticmethod
    def valid_proof(last_proof, proof):
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"


# Our blockchain as our API

# Instantiate our node
app = Flask(__name__)

# Generate globally unique address or this node
node_identifier = str(uuid4()).replace('-', '')

# Instantiate the blockchain
blockchain = Blockchain()

@app.route('/mine', methods = ['GET'])
def mine():
    return 'We will mine a new Block.'

@app.route('/transactions/new', methods = ['POST'])
def new_transactions():
    return "We'll add new transaction."

@app.route('/chain', methods = ['GET'])
def full_chain():
    response = {
        'chain' : blockchain.chain,
        'lenght' : len(blockchain.chain),
    }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5000)