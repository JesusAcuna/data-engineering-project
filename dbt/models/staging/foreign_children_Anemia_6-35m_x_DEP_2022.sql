{{ config(materialized="table") }}

select *,
    CAST('2022-03-01' as date) as Date_range,
    '3-years-old foreign children' as Category, 
    from {{ source("staging", "foreign_children_Anemia 6-35m x DEP_2022_01_03") }}
UNION ALL 
select *,
    CAST('2022-06-01' as date) as Date_range,
    '3-years-old foreign children' as Category, 
    from {{ source("staging", "foreign_children_Anemia 6-35m x DEP_2022_01_06") }}
UNION ALL
select *,
    CAST('2022-09-01' as date) as Date_range,
    '3-years-old foreign children' as Category, 
    from {{ source("staging", "foreign_children_Anemia 6-35m x DEP_2022_01_09") }}