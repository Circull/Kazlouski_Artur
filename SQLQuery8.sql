USE [HW3]
GO

SELECT [Time]
      ,[Energy_delta]
      ,[globalnoe_gorizont_izluchenie]
      ,[temperatura]
      ,[Wlagnost]
      ,[Skoroct_wetra]
      ,[Oblachnost]
      ,[Wremja_solnechnogo_sveta]
      ,[Dlina_dnja]
      ,[SunlightTime/daylength]
  FROM [dbo].[R]

GO

SELECT [Energy_delta] FROM [dbo].[R]
WHERE [Time] = '1.1.2017 1:30'

SELECT [Energy_delta] FROM [dbo].[R]
WHERE [Time] BETWEEN '1.1.2017 10:00' AND '1.1.2017 10:45' 

SELECT [Time], [Energy_delta], [globalnoe_gorizont_izluchenie], [temperatura], [Wlagnost], [Skoroct_wetra], [Oblachnost], [Wremja_solnechnogo_sveta], 
[Dlina_dnja], [SunlightTime/daylength] FROM [dbo].[R]
WHERE [Wlagnost] = 64 AND [Oblachnost] = 2

SELECT MAX(Energy_delta) AS MAXIMUM_ENERGY_DELTA FROM R
SELECT SUM(Energy_delta) AS SUMMA_ENERGY_DELTA FROM R
WHERE [Time] BETWEEN '1.1.2017 0:00' AND '12.31.2017 23:45'