import lib_business

from flask import Flask, request, render_template

def process(request):
    html_file = 'form01.html'
    try:
        if request.method != 'POST':
            return render_template(html_file, result='')
        
        param01 = request.form.get('param01')
        param02 = request.form.get('param02')
        param03 = request.form.get('param03')
        param04 = request.form.get('param04')
        param05 = request.form.get('param05')
        if not param01 or not param02 or not param03 or not param04 or not param05:
            return render_template(html_file, result="ERROR: Parameters required")
        
        data_json = {
            "a": [param01],
            "b": [param02],
            "c": [param03],
            "d": [param04],
            "e": [param05]
        }
        result = lib_business.prediction(data_json)
        return render_template(html_file, result=result)
    
    except Exception as e:
        return render_template(html_file, result='ERROR: '+e.args[0])
    
    
