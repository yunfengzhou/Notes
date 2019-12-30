Sub AutoCharts()
' 导出所有的excel图表到ppt
    Dim ppt_app As Object, ppt_file As Object, slide As Object
    Dim ws As worksheet, cht As ChartObject

    Set ppt_app = CreateObject("PowerPoint.Application")
    Set ppt_file = ppt_app.Presentations.Add
    

    For i = 1 To ActiveWorkbook.Worksheets.Count
        Set ws = ThisWorkbook.Sheets(i)
        For Each cht in ws.ChartObjects
            cht.Copy
            Set slide = ppt_file.slides.Add(ppt_file.slides.Count+1,11)
            slide.Shapes.Paste            
        Next cht        
    Next
    
    
    recent_time = Day(Date) & Hour(Time) & Minute(Time) & Second(Time)
    name_without_xlsx = Left(ActiveWorkbook.Name, InStr(ActiveWorkbook.Name, ".") - 1)
    name_update = name_without_xlsx & recent_time
    
    ppt_file.SaveAs Filename:=Application.ActiveWorkbook.Path & "\" & name_update

    ' ppt_file.SaveAs("C:\Users\yunfe\Desktop\test\name_update.pptx")
End Sub



Sub AutoCharts()
' 导出当前页面的excel图表到ppt
    Dim ppt_app As Object, ppt_file As Object, slide As Object
    Dim ws As worksheet, cht As ChartObject

    Set ppt_app = CreateObject("PowerPoint.Application")
    Set ppt_file = ppt_app.Presentations.Add
    

    
    Set ws = ActiveWorkbook.ActiveSheet
    For Each cht in ws.ChartObjects
        cht.Copy
        Set slide = ppt_file.slides.Add(ppt_file.slides.Count+1,11)
        slide.Shapes.Paste            
    Next cht        
    
    
    
    recent_time = Day(Date) & Hour(Time) & Minute(Time) & Second(Time)
    name_without_xlsx = Left(ActiveWorkbook.Name, InStr(ActiveWorkbook.Name, ".") - 1)
    name_update = name_without_xlsx & recent_time
    
    ppt_file.SaveAs Filename:=Application.ActiveWorkbook.Path & "\" & name_update

    ' ppt_file.SaveAs("C:\Users\yunfe\Desktop\test\name_update.pptx")
End Sub

