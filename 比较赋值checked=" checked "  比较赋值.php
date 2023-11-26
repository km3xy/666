比较赋值 checked=" checked " 
//扩展方案  先随机比较选中input   然后再范围内随机
//流程控制，比较选中input
//checked=" checked "  比较赋值
// if ($t>$x && $t>$e  &&  $x>$e  )
//条件成立赋值，不成立不赋值

//可以加入浮点数
// 生成0~1之间的随机浮点数
$random_float = mt_rand()/mt_getrandmax();
echo $random_float;
上述代码会生成0到1之间的一个随机浮点数

4s5r   4舍5入


 <label>
     
  <input type="checkbox" name="ccc[1]" id="ccc" value="66666666666666666">随机选中input点我,这里是控制开关

 </label>

  <label>
     
  <input type="checkbox" 
  
<?php 

$t=$_POST['ccc'];  

$x=mt_rand()/mt_getrandmax();

$e=mt_rand()/mt_getrandmax();

//$x=mt_rand();

//$e=mt_rand();



if ($t>$x && $t>$e  &&  $x>$e  )

{ 


echo  "checked";

} 


?>
  

  name="a[1]" id="c" value="666">666

   </label>



















