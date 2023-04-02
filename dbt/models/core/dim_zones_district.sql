{{config(materialized="table")}}

select ubigeo_inei,
       latitud,
       longitud
from {{ref('ubigeous_lookup')}}
 