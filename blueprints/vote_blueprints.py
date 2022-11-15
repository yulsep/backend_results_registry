from flask import Blueprint, jsonify
from flask import request

from controllers.vote_controller import VoteController

vote_blueprints = Blueprint('vote_controller', __name__)
vote_controller = VoteController()


@vote_blueprints.route("/vote/all", methods=["GET"])
def get_all_vote():
    response = vote_controller.index()
    return jsonify(response), 200


@vote_blueprints.route('/vote/<string:id_>', methods=['GET'])
def get_votes_by_id(id_):
    response = vote_controller.show(id_)
    return jsonify(response), 200


@vote_blueprints.route("/vote/insert", methods=["POST"])
def vote_insert():
    vote = request.get_json()
    response = vote_controller.create(vote)
    return jsonify(response), 201


@vote_blueprints.route("/vote/update/<string:id_>", methods=["PATCH"])
def vote_update(id_):
    vote = request.get_json()
    response = vote_controller.update(id_, vote)
    return jsonify(response), 201


@vote_blueprints.route("/vote/<string:vote_id>/table/<string:table_id>", methods=['PUT'])
def assign_table(vote_id, table_id):
    response = vote_controller.table_assign(vote_id, table_id)
    return response, 201



@vote_blueprints.route("/vote/delete/<string:id_>", methods=["DELETE"])
def vote_delete(id_):
    response = vote_controller.delete(id_)
    return jsonify(response), 204
