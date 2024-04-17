select *
from patients
where substr(conditions,1,5)='DIAB1'
or conditions like '% DIAB1%'
