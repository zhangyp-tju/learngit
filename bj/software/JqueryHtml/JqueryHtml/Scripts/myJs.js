$(document).ready(function () {
    $("#btnckb1").bind("click", CkboxDisabled);
    $("#btnckb2").bind("click", GetCkboxValues);
    $("#btnckb3").bind("click", CkboxAllChecked);
    $("#btnckb4").bind("click", CkboxAllNoChecked);
    $("#btnckb5").bind("click", CkboxTurnChecked);

    $("#btnRia1").bind("click", RdbtnDisabled);
    $("#btnRia2").bind("click", GetRdbtnValues);
    $("#btnRia3").bind("click", RdbtnLastChecked);

    $("#btnCbx1").bind("click", CbxDisabled);
    $("#btnCbx2").bind("click", GetCbxSelected);
    $("#btnCbx3").bind("click", CbxLastSelected);
    $("#btnCbx4").bind("click", CbxGetSelectIndex);
    $("#btnCbx5").bind("click", CbxClearOption);
    $("#btnCbx6").bind("click", CbxAddOption);
});

/* CheckBox 
选择
(1)选择所有的 checkbox  控件
//根据input类型选择
$("input[type=checkbox]")  //等同于文档中的 $("input:checkbox")
//根据名称选择
$("input[name=checkbox]") 
     
(2)根据索引获得 checkbox 控件
$("input[name=ckb]:eq(1)") //结果返回：<input id="ckb2" name="ckb" value="1" type="checkbox" /><span>排球</span>
   
(3)获得所有禁用的 checkbox 控件
$("input[type=checkbox]:disabled") 
结果返回：
        <input id="ckb3" name="ckb" disabled="disabled" value="2" type="checkbox" /><span>乒乓球</span>
        <input id="ckb4" name="ckb" disabled="disabled" value="3" type="checkbox" /><span>羽毛球</span>

(4)获得所有启用的checkbox控件
$("input:checkbox[disabled=false]")
结果返回：
        <input id="ckb1" name="ckb" checked="checked" value="0" type="checkbox" /><span>篮球</span>
        <input id="ckb2" name="ckb" checked="checked" value="1" type="checkbox" /><span>排球</span>

(4)获得所有checked的checkbox控件
$("input:checkbox:checked") //等同于 $("input[type=checkbox][checked]")
结果返回：
        <input id="ckb1" name="ckb" checked="checked" value="0" type="checkbox" /><span>篮球</span>
        <input id="ckb2" name="ckb" checked="checked" value="1" type="checkbox" /><span>排球</span>

(5)获取所有未checkde的checkbox控件
$("input:checkbox:[checked=false]") 等同于 $("input[type=checkbox][checked=false]")
结果返回：
        <input id="ckb3" name="ckb" disabled="disabled" value="2" type="checkbox" /><span>乒乓球</span>
        <input id="ckb4" name="ckb" disabled="disabled" value="3" type="checkbox" /><span>羽毛球</span>

(6)获得value 为 0 的checkbox 控件
$("input[type=checkbox][value=0]") 结果返回：<input id="ckb1" name="ckb" checked="checked" value="0" type="checkbox" /><span>篮球</span>

禁用:
(1)禁用所有的checkbox控件：
   $("input:checkbox").attr("disabled", true) 

(2)启用某些禁用的 checkbox 控件
   $("input[type=checkbox]:disabled").attr("disabled", false);

(3)判断value=0的checkbox是否禁用
    if ($("input[name=ckb][value=0]").attr("disabled") == true) {
        alert("不可用");
    }
    else {
        alert("可用");
    }
Checked：
 (1)全选：
 $("input:checkbox").attr("checked", true);
 
 (2)全不选
 $("input:checkbox").attr("checked", false);

 (3)反选：
 $("input:checkbox").each(function () {
        if ($(this).attr("checked")) {
            //$(this).removeAttr("checked");
            $(this).attr("checked", false);
        }
        else {
            $(this).attr("checked",true);
        }
  });

获取值：
function GetCkboxValues() {
    var str="";
    $("input:checkbox:checked").each(function () {
    
        switch ($(this).val()) {
            case "0":
                str += "篮球,";
                break;
            case "1":
                str += "排球,";
                break;
            case "2":
                str += "乒乓球,";
                break;
            case "3":
                str += "羽毛球,";
                break;
        }
    });
    str=str.substring(0, str.length - 1)
}
*/

//禁用所有checkbox
function CkboxDisabled() {
    //禁用所有的checkbox
    $("input:checkbox").attr("disabled", true); // $("input[name=ckb]").attr("disabled", true);

    //启用禁用的 checkbox
    //$("input[type=checkbox]:disabled").attr("disabled", false);    

    //禁用启用的checkbox控件
    //$("input:checkbox[disabled=false]").attr("disabled", true)
    //判断value=0的checkbox是否禁用
    /*
    if ($("input[name=ckb][value=0]").attr("disabled") == true) {
        alert("不可用");
    }
    else {
        alert("可用");
    }
    */
    //禁用cheked标记的checkbox控件
    //$("input:checkbox:checked").attr("disabled", true);

    //禁用未cheked标记的checkbox控件
    //$("input:checkbox:[checked=false]").attr("disabled", true);
}

//获取checkbox选择的数据
function GetCkboxValues() {
    var str="";
    $("input:checkbox:checked").each(function () {
    
        switch ($(this).val()) {
            case "0":
                str += "篮球,";
                break;
            case "1":
                str += "排球,";
                break;
            case "2":
                str += "乒乓球,";
                break;
            case "3":
                str += "羽毛球,";
                break;
        }
    });
    str = str.substring(0, str.length - 1);
    alert(str);
}

//全选 checkbox 
function CkboxAllChecked() {
    $("input:checkbox").attr("checked", true);
}

//全不选 checkbox
function CkboxAllNoChecked() {
    $("input:checkbox").attr("checked", false);
}

//反选 checkbox
function CkboxTurnChecked() {
    $("input:checkbox").each(function () {
        if ($(this).attr("checked")) {
            //$(this).removeAttr("checked");
            $(this).attr("checked", false);
        }
        else {
            $(this).attr("checked",true);
        }
    });
}


/* RadioButton 
选择
(1)选择所有的 RadioButton  控件
//根据input类型选择
$("input[type=radio]")  //等同于文档中的 $("input:radio")
//根据名称选择
$("input[name=edu]") 
     
(2)根据索引获得 RadioButton 控件
$("input:radio:eq(1)") //结果返回：<input name="edu" value="1" type="radio" /><span>本科</span>
   
(3)获得所有禁用的 RadioButton 控件
$("input:radio:disabled") 
结果返回：
        <input name="edu" value="2" type="radio" disabled="disabled" /><span>研究生</span>
        <input name="edu" value="3" type="radio" disabled="disabled"/><span>博士生</span>

(4)获得所有启用的 RadioButton 控件
$("input:radio[disabled=false]")
结果返回：
        <input name="edu" value="0" type="radio" checked="checked" /><span>专科</span>
        <input name="edu" value="1" type="radio" /><span>本科</span>

(4)获得checked的 RadioButton 控件
$("input:radio:checked") //等同于 $("input[type=radio][checked]")
结果返回：
      <input name="edu" value="0" type="radio" checked="checked" /><span>专科</span>

(5)获取未checked的 RadioButton 控件
$("input:radio[checked=false]").attr("disabled", true);
结果返回：
        <input name="edu" value="1" type="radio" /><span>本科</span>
        <input name="edu" value="2" type="radio" disabled="disabled" /><span>研究生</span>
        <input name="edu" value="3" type="radio" disabled="disabled"/><span>博士生</span>

(6)获得value 为 0 RadioButton 控件
$("input[type=radio][value=0]") 结果返回：<input name="edu" value="0" type="radio" checked="checked" /><span>专科</span>

取值：
$("input:radio:checked").val() 

代码选中：
$("input:radio[value=1]").attr("checked", true);

*/

//禁用所有Radiobutton
function RdbtnDisabled() {
    //禁用所有的RadioButton
    $("input:radio").attr("disabled", true);
    //$("input[name=edu]").attr("disabled", true);

    //禁用某个RadioButton控件
    //$("input:radio:eq(1)").attr("disabled", true);

    //启用禁用的RadioButton控件
    //$("input:radio:disabled").attr("disabled", false);

    //禁用当前已经启用的RadioButton控件
    //$("input:radio[disabled=false]").attr("disabled", true);

    //禁用 checked 的RadioButton控件
    //$("input[type=radio][checked]").attr("disabled", true);

    //禁用未checked 的RadioButton控件
    //$("input:[type=radio][checked=false]").attr("disabled", true);

    //禁用value=0 的RadioButton
    //$("input[type=radio][value=0]").attr("disabled", true);
}

//获取RadioButton选择的数据
function GetRdbtnValues() {
    var v = "";
    switch ($("input:radio:checked").val()) {
        case "0":
            v = "专科";
            break;
        case "1":
            v = "本科";
            break;
        case "2":
            v = "硕士";
            break;
        case "3":
            v = "博士";
            break;
    }
    alert(v);
}

//选择本科RadioButton
function RdbtnLastChecked() {

    var v = $("input:radio[value=1]").attr("checked");
    if (!v) {
        $("input:radio[value=1]").attr("checked", true);
    }

    //根据索引控制
    //$("input:radio[name=edu]").get(1).checked = true;
    
    
}

/* ComBox 控件
选择：
 (1)选择selected 下所有option
    $("select option")
    结果：   <option value="0">黑猫警长</option>
            <option value="1" disabled="disabled">大头儿子</option>
            <option value="2">熊出没</option>
            <option value="3">喜羊羊</option>
  (2)选择 selected 下值为2 的 option：
    $("select option[value=2]")
    结果：<option value="2">熊出没</option>
  
  (3)选择色select控件中 disabled 的项：
  $("select option:disabled")
    结果：<option value="1" disabled="disabled">大头儿子</option>

取值：
function GetCbxSelected() {
    var v = $("select option:selected").val();
    switch (v) {
        case "0":
            v = "黑猫警长";
            break;
        case "1":
            v = "大头儿子";
            break;
        case "2":
            v = "熊出没";
            break;
        case "3":
            v = "喜羊羊";
            break;
    }
    alert(v);
}

代码控制选择：
function CbxLastSelected() {

    var v = $("select option[value=2]").attr("selected");
    if (!v) {
        $("select option[value=2]").attr("selected", true);
    }
}


*/

//禁用Combbox控件
function CbxDisabled() {
    //禁用select 控件
    //$("select").attr("disabled", true);

    //禁用select中所有option
    //$("select option").attr("disabled", true);

    //禁用value=2 的option
    //$("select option[value=2]").attr("disabled", true);

    //启用被禁用的option
    //$("select option:disabled").attr("disabled", false);

}

//获取Combox控件选择的数据
function GetCbxSelected() {
    var v = $("select option:selected").val();
    var t = $("select option:selected").text();
    alert("值:" + v + "文本:" + t);
}

//代码控制选择
function CbxLastSelected() {

    //option 值为 2 的被选择
//    var v = $("select option[value=2]").attr("selected");
//    if (!v) {
//        $("select option[value=2]").attr("selected", true);
//    }

    //索引=2 的option 项 被选择
    $("select")[0].selectedIndex = 2; //等同于 $("select option[index=2]").attr("selected", true);
}

//获取选中项的索引
function CbxGetSelectIndex() {

    //获取选中项索引 get 是转换成了dom元素 不是jq对象了
    var selectIndex = $("select").get(0).selectedIndex; //等同于 var selectIndex = $("select option:selected").attr("index");
    alert("选中项索引:" + selectIndex);

    //获取最大的索引
    var maxIndex = $("select option:last").attr("index") //等同于  var maxIndex = $("select option").length - 1;
    alert("最大索引:" + maxIndex);
}

//删除select 控件中的option
function CbxClearOption() {
    //清空所有option
    //$("select option").empty();

    //删除 value=2 的option
    //$("select option[value=2]").remove();

    //删除第一个option
    //$("select option[index=0]").remove();

    //删除 text="熊出没" 的option(不管用)
    //$("select option[text=熊出没]").remove(); each 中不能用break 用return false 代替，continue 用 return true 代替
    $("select option").each(function () {
        if ($(this).text() == "熊出没") {
            $(this).remove();
            return false;
        }
    });
}



function CbxAddOption() {
    //在首位置插入 option 并选择
    //$("select").prepend("<option value='0'>请选择</option>");
    //$("select option[index=0]").attr("selected", true);

    //在尾位置插入 option 并选择
    //获取最大的索引值
    //$("select").append("<option value=\"5\">哪吒闹海</option>");
    //var maxIndex = $("select option:last").attr("index")
    //$("select option[index=" + maxIndex + "]").attr("selected", true);

    //第一个option 项之后插入 新的option 并选择
    //$("<option value=\"5\">哪吒闹海</option>").insertAfter("select option[index=0]"); //等同于
    $("select option[index=0]").after("<option value=\"5\">哪吒闹海</option>");
    $("select option[index=1]").attr("selected", true);
    
}

