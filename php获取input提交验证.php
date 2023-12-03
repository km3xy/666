<html>


<form action="b.php" method="POST">


<input type="checkbox" value=10 name="list">


  <input style="font-size:15px;color:#FF0000" type="submit" data-inline="true"    
  
 name="tj"  value="点我提交开始">




<?php
if(!isset($_POST['tj'])) //如果没提交表单显示以下
{

}
else{
if($_POST['list']==10)
{
echo "选择";
}else
{
echo "未选择";
}
}


?>



</form>

</html>
