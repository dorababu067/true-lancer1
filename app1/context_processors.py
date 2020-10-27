def custom_context_prc(request):
    if request.session.get('user'):
        user = request.session['user']
        return {"username":user}
    else:
        return {"username":"Anonymus"}
