{{ config(materialized="table") }}

select *,
    CAST('2022-03-01' as date) as Date_range,
    '5-years-old children' as Category, 
    from {{ source("staging", "children_EN 0-59m x DEP_2022_01_03") }}
UNION ALL 
select *,
    CAST('2022-06-01' as date) as Date_range,
    '5-years-old children' as Category, 
    from {{ source("staging", "children_EN 0-59m x DEP_2022_01_06") }}
UNION ALL
select *,
    CAST('2022-09-01' as date) as Date_range,
    '5-years-old children' as Category, 
    from {{ source("staging", "children_EN 0-59m x DEP_2022_01_09") }}