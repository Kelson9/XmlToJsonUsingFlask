import flask
from flask import request, jsonify
import  webservice as webservices

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/api/v1/validate', methods=['GET'])
def api_all():
    # take in xml file path
    xml_path = './xml.xml'
    xsd_path = './xsd.xsd'

    if xml_path and xsd_path:
        response = webservices.validate(xml_path,xsd_path)
        if response['status']==200:
           isValid =response['result']
           if isValid:
              json_data = webservices.toJson()
              return jsonify({'status':200,"isValid":isValid,'jsonData':json_data})
           
           else:
              return jsonify({'status':422,"isValid":isValid,'jsonData':Null})
        else:
             return jsonify({'message':response})

        
    else:
        if not xml_path:
           return jsonify({'error':'An XML file path is required!'})
        elif not xsd_path:
             return jsonify({'error':'An XSD file path is required!'})
        else:
             return jsonify({'error':'An XML and XSD file path is required!'})

    


    



app.run()