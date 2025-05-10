from flask_restful import Resource, reqparse
import random
window_size=10

items = {
    "p": "Prime",
    "f": "Fibonacci",
    "e": "even",
    "r":"random numbers"
}   

parser = reqparse.RequestParser()
parser.add_argument("num_type", type=str, required=True, help="enter the numtype")
class AverageCalculator(Resource):
    def get(self, item_id):
        item = items.get(item_id)
        if not item:
            return {"error": "Item not found"}, 404
        if item == "Prime":
            result = self.generate_primes()
        elif item == "Fibonacci":
            result = self.fibonacci()
        elif item == "even":
            result = self.even()
        elif item == "random numbers":
            result = self.random()
        else:
            return {"error": "Unknown num_type"}, 400
        
        return {"type": item, "data": result}, 200

    def post(self, item_id):
        if item_id in items:
            return {"error": "Item already exists"}, 400
        data = parser.parse_args()
        items[item_id] = data
        return data, 201

    def put(self, item_id):
        data = parser.parse_args()
        items[item_id] = data
        return data, 200

    def delete(self, item_id):
        if item_id not in items:
            return {"error": "Item not found"}, 404
        del items[item_id]
        return {"message": "Item deleted"}, 204
    @staticmethod
    def generate_primes():
        return [random.randint(2, 100) for _ in range(window_size)]
    @staticmethod
    def fibonacci():
        sequence = []
        a, b = 0, 1
        for _ in range(window_size):
            sequence.append(a)
            a, b = b, a + b
        return sequence
    @staticmethod
    def even():
        return [i * 2 for i in range(window_size)]
    @staticmethod
    def random():
        return [random.randint(1, 100) for _ in range(window_size)]
