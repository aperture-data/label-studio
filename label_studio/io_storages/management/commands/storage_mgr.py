from django.core.management.base import BaseCommand, CommandError
from label_studio.io_storages.all_api import _get_common_storage_list
from label_studio.io_storages.base_models import ImportStorage
from projects.models import Project
import json


class Command(BaseCommand):
    help = 'Maninpulates the storage on a project'
    def add_arguments(self,p):
        p.add_argument('-s', '--storage', default=None, required=True, type=str, help="Storage provider to use")
        p.add_argument('-t', '--type', default="import", choices=["import","export"], type=str, help="Storage type to use")
        p.add_argument('-p', '--project',default=None,required=True,type=int, help="Project to act on")
        p.add_argument('-a', '--action', default=None, choices=["add", "delete","list"], required=True, type=str, help="Action to take")
        p.add_argument('-c', '--config-json', default=None,  required=False, type=str, help="Path to json config file to configure a storage")
    def handle(self, *args, **options):
        had_storage=False

        if options['action'] == "list":
            proj = Project.objects.get(id=options['project'])
            if proj is None:
                raise ValueError(f"Project {options['project']} doesn't exist")
            storage_objects = []
            self.stdout.write(f"Configured {options['type']} storage {options['storage']}:")
            for api_cfg in _get_common_storage_list():
                if api_cfg['name'] == options['storage']:
                    api_class = api_cfg[f"{options['type']}_list_api"]
                    storage_class = api_class.serializer_class.Meta.model
                    storage_objects += list(storage_class.objects.filter(project=proj))

            if len(storage_objects) == 0:
                self.stdout.write("(None)")
            for o in storage_objects: 
                self.stdout.write(f"* {o.id} \"{o.title}\" {o.meta}")
        elif options['action'] == "add":
            for api_cfg in _get_common_storage_list():
                if api_cfg['name'] == options['storage']:
                    proj = Project.objects.get(id=options['project'])
                    if proj is None:
                        raise ValueError(f"Project {options['project']} doesn't exist")
                    had_storage=True
                    api_class = api_cfg[f"{options['type']}_list_api"]
                    api_object = api_class()
                    create_data= { 'project':proj,'title':"Managemnt tool created {options['type']}"}

                    if options['config_json'] != None:
                        with open(options['config_json'], 'r') as fp:
                            from_json = json.loads(fp.read())
                            create_data.update(from_json)

                    api_object.request = None
                    api_object.format_kwarg = None
                    serializer=api_object.get_serializer(data={}) 
                    try:
                        serializer.validate(data=create_data)
                        serializer.create(validated_data=create_data)
                        self.stdout.write(f"Created {options['type']} {options['storage']} for project {options['project']}")
                    except Exception as e:
                        self.stderr.write(f"Failed creating storage: {e}")
