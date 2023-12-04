<html>

    

<form method="post" action="tjdl123456789tj.php">
      
<h1>

 <fieldset data-role="controlgroup" data-type="horizontal">

<br>

  <input style="font-size:65px;color:#FF0000" type="submit" data-inline="true" 
name="tj"   value="点我提交开始">

<a href="tjdl123456789tj.php" style="font-size:25px;">清空返回还原</a>


<h1>

 
 
  <label>
     
  <input type="checkbox" 
  
name="c1" id="c" value="1">1
 <br>
 
<?php 
$x=$_POST['c1'];

$y=mt_rand()/mt_getrandmax();

$e=mt_rand()/mt_getrandmax();


if(!isset($_POST['tj'])) //如果没提交表单显示以下
{

}
else{
if($x==1  &&  $y<$e)     
{
   echo  mt_rand()/mt_getrandmax();
}else
{
echo "未选择";
}
}


?>

 </label>

 <label>
     
  <input type="checkbox"           name="2" id="c2" value="2">2
  
 <br>
  
<?php 


$x=$_POST['c2'];


$y=mt_rand()/mt_getrandmax();

$e=mt_rand()/mt_getrandmax();


if(!isset($_POST['tj'])) //如果没提交表单显示以下
{

}
else{
if($x==2  &&  $y<$e)     
{
   echo  mt_rand()/mt_getrandmax();
}else
{
echo "未选择";
}
}


?>

 </label>
 <label>
     
  <input type="checkbox"           name="3" id="c3" value="3">3
  
 
 <br>
  
<?php 

$x=$_POST['c3'];
$y=mt_rand()/mt_getrandmax();

$e=mt_rand()/mt_getrandmax();


if(!isset($_POST['tj'])) //如果没提交表单显示以下
{

}
else{
if($x==3  &&  $y<$e)     
{
   echo  mt_rand()/mt_getrandmax();
}else
{
echo "未选择";
}
}

?>
 </label>

 <label>
     
  <input type="checkbox"           name="4" id="c4" value="4">4
 <br>
<?php 

$x=$_POST['c4'];

$y=mt_rand()/mt_getrandmax();

$e=mt_rand()/mt_getrandmax();

if(!isset($_POST['tj'])) //如果没提交表单显示以下
{

}
else{
if($x==4  &&  $y<$e)     
{
   echo  mt_rand()/mt_getrandmax();
}else
{
echo "未选择";
}
}


?>


 </label>

 <label>
     
  <input type="checkbox"           name="5" id="c5" value="5">5
  
 <br>

<?php 

$x=$_POST['c5'];

$y=mt_rand()/mt_getrandmax();

$e=mt_rand()/mt_getrandmax();

if(!isset($_POST['tj'])) //如果没提交表单显示以下
{

}
else{
if($x==5  &&  $y<$e)     
{
   echo  mt_rand()/mt_getrandmax();
}else
{
echo "未选择";
}
}

?>

 </label>



