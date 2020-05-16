Sub Export_emf()
    Const ppLayoutBlank = 12
    Const msoTrue = -1
    Const msoFalse = 0
    Const ppShapeFormatGIF = 0
    Const ppShapeFormatJPG = 1
    Const ppShapeFormatPNG = 2
    Const ppShapeFormatBMP = 3
    Const ppShapeFormatWMF = 4
    Const ppShapeFormatEMF = 5
'    Dim oPPT
    Dim oPPT As PowerPoint.Application
    '创建ppt对象
'    Set oPPT = VBA.CreateObject("PowerPoint.Application")
    With PowerPoint.Application
        '使得ppt可见
        .Visible = msoTrue
'        Dim oPresentation Dim 变量名称 as 数据类型
        Dim oPresentation As PowerPoint.Presentation
        '获取ppt演示文稿对象
        If .Presentations.Count > 0 Then
            Set oPresentation = .Presentations(1)
        Else
            Set oPresentation = Presentations.Add
        End If
        With oPresentation
            '获取幻灯片对象
''           Dim oSlide As Slide
'            Dim oSlide
            Dim i As Long
            For i=1 to .Slides.Count
                Set oSlide = .Slides(i)
                With oSlide
                    Dim oSP As Shape
                    Dim j As Long
                    j=1
                    For Each oSP In .Shapes
                        With oSP
                            ' Dim recent_time As Time
                            recent_time = Day(Date) & Hour(Time) & Minute(Time) & Second(Time)
                            
                            ' sName = oSlide.Name & "time" & recent_time & "NO." & j
                            ' SlideIndex返回当前相对编号，Name和SlideID均返回创建时的绝对值
                            sName = "P" & oSlide.SlideIndex & "time" & recent_time & "NO." & j
                            
                            sFilename = PowerPoint.ActivePresentation.Path & "\" & sName & ".emf"
                            ' 导出为emf图片格式
                            .Export sFilename, ppShapeFormatEMF                            
                        End With
                        j=j+1
                    Next  
                End With
            Next
            MsgBox("Pictures have been exported successfully")            
        End With
    End With
End Sub