window.onload = function()
{
    var oFCKeditor = new FCKeditor('id_body') ;
    oFCKeditor.BasePath = "/media/FCKeditor/" ;
    oFCKeditor.ToolbarSet = "Default" ;
    oFCKeditor.Width = "100%";
    oFCKeditor.Height = 400 ;
    oFCKeditor.ReplaceTextarea() ;
}
