def find_all(pagination, person_type, filters):
    try:
        list_results = []
        people = PersonModel.select().join(UserLoginModel, peewee.JOIN.LEFT_OUTER, on=(UserLoginModel.person_id == PersonModel.id)).join(ResponsableModel, peewee.JOIN.LEFT_OUTER, on=(ResponsableModel.person_id == PersonModel.id)).join(PatientResponsableModel, peewee.JOIN.LEFT_OUTER, on=(PatientResponsableModel.responsable_id == ResponsableModel.person_id)).join(PatientHospitalModel, peewee.JOIN.LEFT_OUTER, on=(PatientHospitalModel.patient_id == PatientResponsableModel.patient_id)).join(HospitalModel, peewee.JOIN.LEFT_OUTER, on=(HospitalModel.id == PatientHospitalModel.hospital_id)).where((PersonModel.person_type == person_type) & (UserLoginModel.status == 'active') & (reduce(operator.and_, filters.get_clauses()))).order_by(PersonModel.id).paginate(pagination.get_current_page(), pagination.get_paginate_by())
        pagination.set_all_rows(count_people(person_type, filters))
        
        for person in people:
            list_results.append(find_by_id(person))

        return mapping_find_all_responsibles(list_results, pagination)
    except Exception as err:
        raise err

def count_people(person_type, filters):
    total_responsables = PersonModel.select().join(UserLoginModel, peewee.JOIN.LEFT_OUTER, on=(UserLoginModel.person_id == PersonModel.id)).join(ResponsableModel, peewee.JOIN.LEFT_OUTER, on=(ResponsableModel.person_id == PersonModel.id)).join(PatientResponsableModel, peewee.JOIN.LEFT_OUTER, on=(PatientResponsableModel.responsable_id == ResponsableModel.person_id)).join(PatientHospitalModel, peewee.JOIN.LEFT_OUTER, on=(PatientHospitalModel.patient_id == PatientResponsableModel.patient_id)).join(HospitalModel, peewee.JOIN.LEFT_OUTER, on=(HospitalModel.id == PatientHospitalModel.hospital_id)).where((PersonModel.person_type == person_type) & (UserLoginModel.status == 'active') & (reduce(operator.and_, filters.get_clauses()))).count()
    return  total_responsables