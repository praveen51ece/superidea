
@dajaxice_register
def unhide_lead(request,id):

    Client = Client.objects.get(id=id)
    Client.display = 0    
    Client.save()
    print " view list"
    return json.dumps({'result': 'saved successfully'})

@dajaxice_register
def hide_lead(request,id):
    
    Client = Client.objects.get(id=id)
    Client.display = 1    
    Client.save()
    print " view list"
    return json.dumps({'result': 'saved successfully'})