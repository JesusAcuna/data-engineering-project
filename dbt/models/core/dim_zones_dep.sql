{{config(materialized="table")}}

select Department,
       Capital,
       concat(Longitude,',',Latitude) as LonLat
from {{ref('lon_lat')}}