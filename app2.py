from flask import url_for
from flask import Flask, render_template, request, redirect
import requests
import re

import matplotlib.pyplot as plt

app = Flask(__name__)

date = ['Thursday', 'Tuesday', 'Sunday', 'Sunday', 'Monday', 'Wednesday', 'Friday', 'Saturday', 'Thursday', 'Monday', 'Sunday', 'Saturday', 'Friday', 'Wednesday', 'Saturday', 'Saturday', 'Friday', 'Saturday', 'Saturday', 'Monday', 'Monday', 'Sunday', 'Tuesday', 'Wednesday', 'Monday', 'Monday', 'Thursday', 'Wednesday', 'Wednesday', 'Tuesday', 'Wednesday', 'Saturday', 'Friday', 'Friday', 'Saturday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Sunday', 'Tuesday', 'Friday', 'Saturday', 'Tuesday', 'Monday', 'Thursday',
        'Monday', 'Wednesday', 'Sunday', 'Wednesday', 'Monday', 'Friday', 'Wednesday', 'Thursday', 'Wednesday', 'Thursday', 'Friday', 'Sunday', 'Wednesday', 'Sunday', 'Monday', 'Friday', 'Monday', 'Monday', 'Saturday', 'Sunday', 'Tuesday', 'Wednesday', 'Saturday', 'Wednesday', 'Tuesday', 'Monday', 'Saturday', 'Friday', 'Thursday', 'Tuesday', 'Friday', 'Thursday', 'Sunday', 'Monday', 'Sunday', 'Monday', 'Thursday', 'Thursday', 'Wednesday', 'Wednesday', 'Monday', 'Wednesday', 'Friday', 'Monday', 'Wednesday', 'Tuesday', 'Sunday', 'Monday', 'Sunday', 'Saturday', 'Sunday', 'Tuesday', 'Thursday', 'Friday', 'Friday', 'Sunday', 'Sunday', 'Sunday', 'Tuesday', 'Wednesday', 'Tuesday', 'Monday', 'Monday', 'Thursday', 'Thursday', 'Tuesday', 'Wednesday', 'Sunday', 'Wednesday', 'Sunday', 'Thursday', 'Wednesday', 'Saturday', 'Sunday', 'Monday', 'Wednesday', 'Saturday', 'Tuesday', 'Wednesday', 'Thursday', 'Monday', 'Saturday', 'Monday', 'Saturday', 'Monday', 'Tuesday', 'Wednesday', 'Monday', 'Saturday', 'Wednesday', 'Thursday', 'Monday', 'Tuesday', 'Thursday', 'Friday', 'Friday', 'Sunday', 'Tuesday', 'Tuesday', 'Tuesday', 'Thursday', 'Tuesday', 'Sunday', 'Wednesday',
        'Monday', 'Tuesday', 'Sunday', 'Tuesday', 'Thursday', 'Wednesday', 'Thursday', 'Monday', 'Tuesday', 'Tuesday', 'Wednesday', 'Saturday', 'Friday', 'Sunday', 'Wednesday', 'Tuesday', 'Sunday', 'Friday', 'Tuesday', 'Saturday', 'Monday', 'Wednesday', 'Sunday', 'Monday', 'Wednesday', 'Sunday', 'Wednesday', 'Wednesday', 'Friday', 'Tuesday', 'Sunday', 'Friday', 'Tuesday', 'Thursday', 'Friday', 'Monday', 'Tuesday', 'Friday', 'Saturday', 'Monday', 'Sunday', 'Friday', 'Wednesday', 'Friday', 'Sunday', 'Tuesday', 'Monday',
        'Friday', 'Monday', 'Thursday']
x = [19, 19, 2, 2, 10, 66, 91, 11, 45, 99, 70, 3, 94, 100, 38, 7, 72, 52, 89, 1, 40, 51, 24, 59, 60, 81, 21, 32, 71, 35, 81, 100, 96, 26, 62, 12, 62, 86, 59, 59, 92, 54, 42, 32, 7, 5, 97, 0, 79, 2, 75, 56, 5, 19, 17, 30, 17, 35, 89, 38, 85, 56, 48, 1, 99, 17, 84, 92, 90, 63, 63, 55, 62, 75, 93, 15, 66, 24, 15, 14, 52, 70, 4, 6, 46, 18, 18, 19, 99, 47, 76, 26, 12, 39, 11, 58, 80, 7, 76, 52, 100, 81, 54, 93, 52, 90, 0, 69, 80, 84, 73, 53, 32, 77, 67, 62, 12, 2, 43, 76, 59, 15, 49, 69, 87, 79, 15, 32, 29, 95, 17, 53,
     62, 61, 96, 76, 36, 45, 25, 13, 53, 11, 100, 80, 63, 22, 18, 89, 71, 39, 59, 14, 15, 3, 12, 36, 91, 98, 29, 87, 35, 6, 24, 20, 69, 77, 23, 87, 76, 81, 0, 56, 0, 91, 88, 38, 64, 8, 21, 77, 22, 41, 92, 8, 9, 92, 1, 24, 32, 79, 93, 85, 79, 66, 53, 58, 32, 76, 43, 8]
y = [2, 40, 22, 47, 3, 9, 22, 16, 32, 6, 2, 6, 10, 34, 8, 17, 23, 3, 8, 41, 16, 11, 28, 45, 22, 30, 41, 12, 22, 42, 23, 40, 40, 28, 11, 8, 13, 38, 12, 21, 20, 32, 45, 16, 6, 31, 49, 43, 18, 38, 23, 16, 28, 23, 10, 12, 47, 28, 6, 36, 10, 13, 16, 20, 38, 29, 16, 26, 0, 42, 7, 32, 35, 45, 23, 13, 6, 49, 8, 44, 14, 34, 26, 7, 43, 2, 3, 6, 37, 2, 9, 3, 40, 25, 30, 2, 30, 9, 45, 19, 43, 18, 39, 27, 6, 1, 10, 26, 4, 19, 9, 11, 4, 3, 43, 33, 16, 11, 15, 31, 0, 26, 42, 49, 42, 28, 11, 28, 26, 40, 41, 50, 20, 30, 6, 1, 8, 41, 10, 6, 39, 2, 14, 35, 6, 29, 8, 0, 40, 32, 37, 8, 13, 28, 40, 34, 34, 29, 11, 29, 34, 30, 16, 1, 43, 50, 27, 27, 9, 11, 39, 7,
     11, 9, 6, 32, 35, 5, 48, 8, 9, 44, 46, 38, 42, 42, 46, 13, 9, 45, 3, 48, 44, 33, 28, 48, 10, 24, 11, 43]

batch_ID = [4, 2, 7, 7, 1, 3, 5, 6, 4, 1, 7, 6, 5, 3, 6, 6, 5, 6, 6, 1, 1, 7, 2, 3, 1, 1, 4, 3, 3, 2, 3, 6, 5, 5, 6, 1, 2, 3, 4, 7, 2, 5, 6, 2, 1, 4, 1, 3, 7, 3, 1, 5, 3, 4, 3, 4, 5, 7, 3, 7, 1, 5, 1, 1, 6, 7, 2, 3, 6, 3, 2, 1, 6, 5, 4, 2, 5, 4, 7, 1, 7, 1, 4, 4, 3, 3, 1, 3, 5, 1, 3, 2, 7, 1, 7, 6, 7, 2,
            4, 5, 5, 7, 7, 7, 2, 3, 2, 1, 1, 4, 4, 2, 3, 7, 3, 7, 4, 3, 6, 7, 1, 3, 6, 2, 3, 4, 1, 6, 1, 6, 1, 2, 3, 1, 6, 3, 4, 1, 2, 4, 5, 5, 7, 2, 2, 2, 4, 2, 7, 3, 1, 2, 7, 2, 4, 3, 4, 1, 2, 2, 3, 6, 5, 7, 3, 2, 7, 5, 2, 6, 1, 3, 7, 1, 3, 7, 3, 3, 5, 2, 7, 5, 2, 4, 5, 1, 2, 5, 6, 1, 7, 5, 3, 5, 7, 2, 1, 5, 1, 4]


def select_data(batch_id, date_from, date_to):
    week = ['Monday', 'Tuesday', 'Wednesday','Thursday', 'Friday', 'Saturday', 'Sunday']
    days = []
    z = None
    for i in week:
        if i == date_from:
            z = 'started'
        if i == date_to:
            days.append(i)
            break
        if z == 'started':
            days.append(i)

    indizes = []
    for i in range(0, len(date)):
        if date[i] in days:
            indizes.append(i)
    x_selected = [x[i] for i in indizes]
    y_selected = [y[i] for i in indizes]

    return x_selected, y_selected

def store(*values):
    store.values = values or store.values
    return store.values

def check_current_parameter(*args):
    url = args[0]
    if re.search(r"http:\/\/localhost:5000\/view\?batch_id=[1-9](&?)from_date=(Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday)(&?)(to_date?)=(Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday)", url):
        return True
    return False

@app.route('/home', methods=['GET', 'POST'])
def home():
    return 'Welcome!, <a href="/select"> Go to Select Page! </a>'

@app.route('/select', methods=['GET', 'POST'])
def select():

    if request.method == 'POST':
        batch_id = request.form['SelectBatchID']
        from_date = request.form['TimeSelectFrom']
        to_date = request.form['TimeSelectTo']
        #g.selected_data = data -> globales Object welches nach jedem kompletten Proess wieder gelöscht wird
        #return requests.post('http://localhost:5000/view', params={'BatchID': batch_id, 'TimeFrom': from_date, 'TimeTo':to_date})
        return redirect(url_for('view', batch_id=batch_id, from_date=from_date, to_date=to_date, **request.args))

    return render_template('select.html')

@app.route('/view', methods=['GET', 'POST'])
def view():

    if request.method == 'POST':
        request_batchID, request_DateFrom, request_DateTo = store()
        return redirect(url_for('process', batch_id=request_batchID, from_date=request_DateFrom, to_date=request_DateTo, **request.args))
    
    request_url = request.url
    request_batchID = request.args.get('batch_id')
    request_DateFrom = request.args.get('from_date')
    request_DateTo = request.args.get('to_date')

    check_url_parameters = check_current_parameter(request_url)

    if check_url_parameters == False:
        return redirect('home')

    x_selected, y_selected = select_data(
        request_batchID, request_DateFrom, request_DateTo)

    store(request_batchID, request_DateFrom, request_DateTo)

    return render_template('view.html', x_selected=x_selected, y_selected=y_selected, len=len(x_selected))

@app.route('/process', methods=['GET', 'POST'])
def process():

    if request.method == 'POST':
        request_batchID, request_DateFrom, request_DateTo = store()
        DeleteData = request.form['DeleteData']
        ExportData = request.form['ExportData']
        ExportPicture = request.form['ExportPicture']
        CopyData = request.form['CopyData']
        WriteProtection = request.form['WriteProtection']

        return redirect(url_for('home', batch_id=request_batchID, from_date=request_DateFrom,
                                to_date=request_DateTo, DeleteData=DeleteData, ExportData=ExportData, ExportPicture=ExportPicture, CopyData=CopyData, WriteProtection=WriteProtection))
    request_batchID = request.args.get('batch_id')
    request_DateFrom = request.args.get('from_date')
    request_DateTo = request.args.get('to_date')

    return render_template('process.html')

if __name__ == "__main__":
    app.run('localhost', port=5000)
