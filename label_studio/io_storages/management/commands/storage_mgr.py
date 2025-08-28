from django.core.management.base import BaseCommand, CommandError
from label_studio.io_storages.all_api import _get_common_storage_list
from label_studio.io_storages.base_models import ImportStorage
from projects.models import Project


class Command(BaseCommand):
    help = 'Maninpulates the storage on a project'
    def add_arguments(self,p):
        p.add_argument('-s', '--storage', default=None, required=True, type=str, help="Storage type to use")
        p.add_argument('-p', '--project',default=None,required=True,type=int, help="Project to act on")
        p.add_argument('-a', '--action', default=None, choices=["add", "delete","list"], required=True, type=str, help="Action to take")
    def handle(self, *args, **options):
        had_storage=False

        if options['action'] == "list":
            proj = Project.objects.get(id=options['project'])
            print(f"Project is {proj}")
            if proj is None:
                raise ValueError(f"Project {options['project']} doesn't exist")
            storage_objects = []
            print(f"For storage {options['storage']} it has:")
            for info in _get_common_storage_list():
                if info['name'] == options['storage']:
                    list_api_class = info['import_list_api']
                    storage_class = list_api_class.serializer_class.Meta.model
                    storage_objects += list(storage_class.objects.filter(project=proj))

            for o in proj.get_all_storage_objects():
                print(f"* {o.id} \"{o.title}\" {o.meta}")
        elif options['action'] == "add":
            for l in _get_common_storage_list():
                if l['name'] == options['storage']:
                    #proj = Project.objects.filter(id=options['project']).first()
                    proj = Project.objects.get(id=options['project'])
                    print(f"Project is {proj}")
                    if proj is None:
                        raise ValueError(f"Project {options['project']} doesn't exist")
                    had_storage=True
                    self.stdout.write(str(l))
                    a = l['import_list_api']
                    nn = a()
                    print(nn)
                    print(dir(nn))
                    d = { 'project':proj,'title':"Created from mgmt!", 'aperturedb_key':'moooooo'}
                    # probably "do generators.create_view"
                    nn.request = None
                    nn.format_kwarg = None
                    sz=nn.get_serializer(data={}) #data=d)
                    #sz=nn.get_serializer(data=d)
                    #print(sz)
                    sz.validate(data=d)
                    sz.create(validated_data=d)
