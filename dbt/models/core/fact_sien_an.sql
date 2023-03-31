{{config(materialized='table')}}

--with VRAEM_children_Anemia_6-35m_x_DISTRITO_2022_01_03 as (
with  dim_zones_dep as (
    select * from {{ ref('dim_zones_dep') }}
    --where latitud is not null and longitud is not null
),

a as (
    select *
    from {{ ref('children_Anemia_6-35m_x_DEP_2022') }}
),
b as (
    select *
    from {{ ref('children_Anemia_6-59m_x_DEP_2022') }}
),
c as (
    select *
    from {{ ref('foreign_children_Anemia_6-35m_x_DEP_2022') }}
),
d as (
    select *
    from {{ ref('foreign_children_Anemia_6-59m_x_DEP_2022') }}
),
e as (
    select *
    from {{ ref('pregnant_women_Anemia_x_DEP_2022') }}
),
children_an_unioned as (
    select * from a
    union all
    select * from b
    union all
    select * from c
    union all
    select * from d
    union all
    select * from e
)
select 
    children_an_unioned.Department,
    children_an_unioned.Date_range,
    children_an_unioned.Category,
    children_an_unioned.Total as Total_A,
    children_an_unioned.AT_Cases as AT_Cases_A,
    children_an_unioned.AT_Rate as AT_Rate_A,
    children_an_unioned.Total-LAG(children_an_unioned.Total,1,0) 
        OVER(PARTITION BY children_an_unioned.Department,children_an_unioned.Category ORDER BY children_an_unioned.Department,children_an_unioned.Date_range) AS Total_M,
    children_an_unioned.AT_Cases-LAG(children_an_unioned.AT_Cases,1,0) 
        OVER(PARTITION BY children_an_unioned.Department,children_an_unioned.Category ORDER BY children_an_unioned.Department,children_an_unioned.Date_range) AS AT_Cases_M,
    children_an_unioned.AL_Cases as AL_Cases_A,
    children_an_unioned.AL_Rate as AL_Rate_A,
    children_an_unioned.AL_Cases-LAG(children_an_unioned.AL_Cases,1,0) 
        OVER(PARTITION BY children_an_unioned.Department,children_an_unioned.Category ORDER BY children_an_unioned.Department,children_an_unioned.Date_range) AS AL_Cases_M,
    children_an_unioned.AM_Cases as AM_Cases_A,
    children_an_unioned.AM_Rate as AM_Rate_A,
    children_an_unioned.AM_Cases-LAG(children_an_unioned.AM_Cases,1,0) 
        OVER(PARTITION BY children_an_unioned.Department,children_an_unioned.Category ORDER BY children_an_unioned.Department,children_an_unioned.Date_range) AS AM_Cases_M,
    children_an_unioned.AS_Cases as AS_Cases_A,
    children_an_unioned.AS_Rate as AS_Rate_A,
    children_an_unioned.AS_Cases-LAG(children_an_unioned.AS_Cases,1,0) 
        OVER(PARTITION BY children_an_unioned.Department,children_an_unioned.Category ORDER BY children_an_unioned.Department,children_an_unioned.Date_range) AS AS_Cases_M,
    dz.LonLat

from children_an_unioned
inner join dim_zones_dep as dz
on children_an_unioned.Department=dz.Department

ORDER BY children_an_unioned.Department, children_an_unioned.Category


