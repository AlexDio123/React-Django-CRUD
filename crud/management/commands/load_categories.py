from xml.etree.ElementTree import fromstring, parse
from django.core.management import BaseCommand
from crud.models import Category
from pathlib import Path
from django.conf import settings
import xml.etree.ElementTree as ET


class Command(BaseCommand):
    help = "Load Categories into models"

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):

        xml_tree = ET.parse(Path(settings.BASE_DIR,'categories.xml'))
        root = xml_tree.getroot()

        ns = {'xmlns': 'urn:ebay:apis:eBLBaseComponents'} #Define the namespace

        for xml_doc in root.findall('xmlns:CategoryArray', ns):  
            for category in xml_doc.findall('xmlns:Category', ns):
                categoryName = category.find("xmlns:CategoryName", ns).text
                categoryLevel = category.find("xmlns:CategoryLevel", ns).text
                categoryParentID = category.find('xmlns:CategoryParentID', ns).text

                models = Category(categoryName= categoryName, categoryLevel= categoryLevel, categoryParentID= categoryParentID)
                models.save()
                print('Categories Succesfully loaded')
