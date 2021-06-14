# Program to convert an xml
# file to json file
  
# import json module and xmltodict
# module provided by python
import json
import xmltodict
from lxml import etree
  
  
# open the input xml file and read
# data in form of python dictionary 
# using xmltodict module
def validate(xml_path: str, xsd_path: str) -> bool:
    
    

    try:  
      
        xmlschema_doc = etree.parse(xsd_path)
        xmlschema = etree.XMLSchema(xmlschema_doc)

        xml_doc = etree.parse(xml_path)
        result = xmlschema.validate(xml_doc)
        return {'status':200, 'result':result}
    # check for XML syntax errors
    except etree.XMLSyntaxError as err:
            error=str(err.error_log).split(':')
            return {'status':500,'error':'error in file "{}" at line {}:{}: {}'.format(error[0],error[1],error[2],error[-1])}
    except:
        return {'status':500,'error':'An unexpected error occured'}

   
    
   



def toJson():
       
    with open("xml.xml") as xml_file:
      
         data_dict = xmltodict.parse(xml_file.read())
         xml_file.close()
      
    # generate the object using json.dumps() 
    # corresponding to json data
      
    json_data = json.dumps(data_dict)

    return json_data
      
    # # Write the json data to output 
    # # json file
    # with open("data.json", "w") as json_file:
    #     json_file.write(json_data)
    #     json_file.close()


 
