from flask_restx import Namespace, Resource, fields
from flask import request, jsonify
from app.models.models import Components

from app.utils.logger import Logger

logger = Logger(__name__)


component_ns = Namespace('api', description="Network component")


component_model = component_ns.model(
    "Components",
    {
        "id":fields.Integer(),
        "name":fields.String()
    }
)

@component_ns.route('/components')
class ComponentsResource(Resource):
    @component_ns.marshal_list_with(component_model)
    def get(self):
        """Get components"""
        logger.logger.info("Requesting all the components")
        return Components.query.all()
    
    @component_ns.marshal_with(component_model)
    @component_ns.expect(component_model)
    def post(self):
        """Post components"""
        logger.logger.info("Creating the components")
        data = request.get_json()

        component_name = data.get('name')
        db_component= Components.query.filter_by(name=component_name).first()

        if db_component is not None:
            return jsonify({"response":"Component already exist"})

        new_component = Components(
            name=data.get('name')
        )

        new_component.save()
        logger.logger.info(f"Successfully created  the components {new_component}")
        return new_component, 201


@component_ns.route('/component/<int:id>')
class ComponentResource(Resource):
    @component_ns.marshal_with(component_model)
    def get(self,id):
        logger.logger.info("Initializing request to get one component")
        component=Components.query.get_or_404(id)
        return component
    
    @component_ns.marshal_with(component_model)
    @component_ns.expect(component_model)
    def put(self, id):
        logger.logger.info(f"Initializing request to update the one component with the id {id}")
        data = request.get_json()

        component_name = data.get('name')
        db_component= Components.query.filter_by(name=component_name).first()

        if db_component is not None:
            return jsonify({"response":"Unable to update the component because already exists"})

        component_to_update = Components.query.get_or_404(id)

        component_to_update.update(data.get("name"))

        logger.logger.info(f"Component {component_name} was updated")
        return component_to_update

    @component_ns.marshal_with(component_model)
    def delete(self, id):
        component=Components.query.get_or_404(id)
        component.delete()
        logger.logger.info(f"Component {component} was deleted")
        return component