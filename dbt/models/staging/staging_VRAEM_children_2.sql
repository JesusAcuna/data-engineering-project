{{config(materialized="table")}}

select 

    cast(Department as string) as Department,
    cast(Province as string) as Province,
    cast(District as string) as District,
    cast(Ubigeous as string) as Ubigeous,
    cast(Total as integer) as Total,
    cast(AT_Cases as integer) as AT_Cases,
    cast(AT_Rate as numeric) as AT_Rate,
    cast(AL_Cases as integer) as AL_Cases,
    cast(AL_Rate as numeric) as AL_Rate,
    cast(AM_Cases as integer) as AM_Cases,
    cast(AM_Rate as numeric) as AM_Rate,
    cast(AS_Cases as integer) as AS_Cases,
    cast(AS_Rate as numeric) as AS_Rate

 from {{source('staging','VRAEM_children_Anemia 6-35m x DISTRITO_2022_01_06')}}