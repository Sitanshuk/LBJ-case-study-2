from django.shortcuts import render
import csv
from datetime import datetime
# Create your views here.

def main(request):
    queryset = {}
    return render(request, "index.html",queryset)

def add(request):
    queryset = {}
    if request.method == 'POST':
        data = request.POST.copy()
        del data['csrfmiddlewaretoken']
        dob = datetime.strptime(data['DateOfBirth'], '%Y-%m-%d')
        data['DateOfBirth'] = datetime.strftime(dob, '%d-%m-%Y')
        with open('students.csv', 'a', newline='') as file:
            fieldnames = ['StudentId','Name','Gender','DateOfBirth','City','State','EmailId','Qualification','Stream']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow(data)
            queryset['success'] = True
    return render(request, "add-student.html",queryset)

def search(request):
    results = list()
    if request.method == 'POST':
        data = request.POST.copy()
        del data['csrfmiddlewaretoken']
        if data:
            with open('students.csv', 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:      
                    for key, value in zip(data.keys(), data.values()):          
                        if row[key] == value:
                            results.append(row)

    return render(request, "search-student.html",{"results" : results})

def display(request):
    StudentList = list()
    with open('students.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            StudentList.append(row)
    return render(request, "display-student.html",{"StudentList" : StudentList})

