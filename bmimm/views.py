from django.shortcuts import render

def bmi_form(request):
    context = {}

    if request.method == 'POST':   
        height = request.POST.get('height', '')  # get as string first
        weight = request.POST.get('weight', '')

        try:
            height_float = float(height)
            weight_float = float(weight)

            bmi = weight_float / ((height_float / 100) ** 2)

            if bmi < 18.6:
                context['message'] = f"You are underweight. BMI: {bmi:.2f}"
                context['alert_class'] = 'alert-danger'
            elif bmi < 24.9:
                context['message'] = f"You are normal. BMI: {bmi:.2f}"
                context['alert_class'] = 'alert-success'
            else:
                context['message'] = f"You are overweight. BMI: {bmi:.2f}"
                context['alert_class'] = 'alert-danger'

        except ValueError:
            context['error'] = "Please enter valid numbers."

        # Pass back the original string values so the inputs keep them
        context['height'] = height
        context['weight'] = weight

    return render(request, 'bmimm/bmi_form.html', context)
