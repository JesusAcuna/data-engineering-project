{{config(materialized='table')}}

--with VRAEM_children_Anemia_6-35m_x_DISTRITO_2022_01_03 as (
with  dim_zones_dep as (
    select * from {{ ref('dim_zones_dep') }}
    --where latitud is not null and longitud is not null
),
a as (
    select *
    from {{ ref('children_EN_0-35m_x_DEP_2022') }}
),
b as (
    select *
    from {{ ref('children_EN_0-59m_x_DEP_2022') }}
),
c as (
    select *
    from {{ ref('foreign_children_EN_0-35m_x_DEP_2022') }}
),
d as (
    select *
    from {{ ref('foreign_children_EN_0-59m_x_DEP_2022') }}
),
children_en_unioned as (
    select * from a
    union all
    select * from b
    union all
    select * from c
    union all
    select * from d
)

select 
    children_en_unioned.Department,
    children_en_unioned.Date_range,
    children_en_unioned.Category,
    children_en_unioned.ITE_DC_Total-LAG(children_en_unioned.ITE_DC_Total,1,0) 
        OVER(PARTITION BY children_en_unioned.Department,children_en_unioned.Category ORDER BY children_en_unioned.Department,children_en_unioned.Date_range) AS ITE_DC_Total_M,
    children_en_unioned.ITE_DC_Cases-LAG(children_en_unioned.ITE_DC_Cases,1,0) 
        OVER(PARTITION BY children_en_unioned.Department,children_en_unioned.Category ORDER BY children_en_unioned.Department,children_en_unioned.Date_range) AS ITE_DC_Cases_M,
    children_en_unioned.ITE_RDC_Total-LAG(children_en_unioned.ITE_RDC_Total,1,0) 
        OVER(PARTITION BY children_en_unioned.Department,children_en_unioned.Category ORDER BY children_en_unioned.Department,children_en_unioned.Date_range) AS ITE_RDC_Total_M,
    children_en_unioned.ITE_RDC_Cases-LAG(children_en_unioned.ITE_RDC_Cases,1,0) 
        OVER(PARTITION BY children_en_unioned.Department,children_en_unioned.Category ORDER BY children_en_unioned.Department,children_en_unioned.Date_range) AS ITE_RDC_Cases_M,
    children_en_unioned.IPE_DG_Total-LAG(children_en_unioned.IPE_DG_Total,1,0) 
        OVER(PARTITION BY children_en_unioned.Department,children_en_unioned.Category ORDER BY children_en_unioned.Department,children_en_unioned.Date_range) AS IPE_DG_Total_M,
    children_en_unioned.IPE_DG_Cases-LAG(children_en_unioned.IPE_DG_Cases,1,0) 
        OVER(PARTITION BY children_en_unioned.Department,children_en_unioned.Category ORDER BY children_en_unioned.Department,children_en_unioned.Date_range) AS IPE_DG_Cases_M,
    children_en_unioned.IPT_DA_Total-LAG(children_en_unioned.IPT_DA_Total,1,0) 
        OVER(PARTITION BY children_en_unioned.Department,children_en_unioned.Category ORDER BY children_en_unioned.Department,children_en_unioned.Date_range) AS IPT_DA_Total_M,
    children_en_unioned.IPT_DA_Cases-LAG(children_en_unioned.IPT_DA_Cases,1,0) 
        OVER(PARTITION BY children_en_unioned.Department,children_en_unioned.Category ORDER BY children_en_unioned.Department,children_en_unioned.Date_range) AS IPT_DA_Cases_M,
    children_en_unioned.IPT_Total-LAG(children_en_unioned.IPT_Total,1,0) 
        OVER(PARTITION BY children_en_unioned.Department,children_en_unioned.Category ORDER BY children_en_unioned.Department,children_en_unioned.Date_range) AS IPT_Total_M,
    children_en_unioned.IPT_RDA_Cases-LAG(children_en_unioned.IPT_RDA_Cases,1,0) 
        OVER(PARTITION BY children_en_unioned.Department,children_en_unioned.Category ORDER BY children_en_unioned.Department,children_en_unioned.Date_range) AS IPT_RDA_Cases_M,
    children_en_unioned.IPT_SP_Cases-LAG(children_en_unioned.IPT_SP_Cases,1,0) 
        OVER(PARTITION BY children_en_unioned.Department,children_en_unioned.Category ORDER BY children_en_unioned.Department,children_en_unioned.Date_range) AS IPT_SP_Cases_M,
    children_en_unioned.IPT_O_Cases-LAG(children_en_unioned.IPT_O_Cases,1,0) 
        OVER(PARTITION BY children_en_unioned.Department,children_en_unioned.Category ORDER BY children_en_unioned.Department,children_en_unioned.Date_range) AS IPT_O_Cases_M,
    dz.LonLat

from children_en_unioned
inner join dim_zones_dep as dz
on children_en_unioned.Department=dz.Department

ORDER BY children_en_unioned.Department,children_en_unioned.Category