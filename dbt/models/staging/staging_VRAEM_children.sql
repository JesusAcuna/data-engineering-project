{{config(materialized="table")}}

select * from {{source('staging','VRAEM_children_Anemia 6-35m x DISTRITO_2022_01_06')}}