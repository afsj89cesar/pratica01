from src.service.service_user import ServiceUser

service = ServiceUser()
resultadoFinal = service.add_user()
print(resultadoFinal)

print(service.store.bd[0].name)
print(service.store.bd[0].job)