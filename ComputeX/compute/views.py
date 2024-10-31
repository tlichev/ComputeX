
from .models import Request, Result
from django.db import transaction

# compute/views.py
import csv
from django.shortcuts import render
from .forms import CSVUploadForm



def compute_view(request):
    result = None
    error = None

    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['file']




            try:
                # Read and process the CSV file
                decoded_file = csv_file.read().decode('utf-8').splitlines()
                reader = csv.DictReader(decoded_file)

                total_sum = 0
                for row in reader:
                    try:
                        a = float(row['A'])
                        b = float(row['B'])
                        operator = row['O']

                        if operator == '+':
                            total_sum += a + b
                        elif operator == '-':
                            total_sum += a - b
                        elif operator == '*':
                            total_sum += a * b
                        elif operator == '/':
                            if b != 0:
                                total_sum += a / b
                            else:
                                raise ValueError("Division by zero error")
                        else:
                            raise ValueError("Unsupported operator")

                        request_record = Request.objects.create(
                            user=request.user,
                            name="CSV Calculation",
                            file_path=csv_file,
                        )
                        Result.objects.create(
                            request=request_record,
                            result=total_sum
                        )

                    except (ValueError, KeyError) as e:
                        error = f"Invalid data format or operator error: {e}"
                        total_sum = None
                        break

                result = total_sum

            except Exception as e:
                error = f"Error processing file: {e}"
        else:
            error = "Please upload a valid CSV file."

    else:
        form = CSVUploadForm()



    return render(request, 'compute/compute.html', {'form': form, 'result': result, 'error': error})
