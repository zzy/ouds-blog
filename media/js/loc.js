//define vars of global in javascript
var MAX_BUILDING_NUMBER = 32 //max building number, and imply that one building, one unit
var MAX_PRODUCE_NUMBER = 4 //max produce sequences for one unit, refer to VIP
var MAX_GOODS_TYPE = 30 //max number of goods' types
function start(){
//if (!document.layers&&!document.all)  //not IE brower???
//return
    this.xmlhttp = null
    //alert(this)
    fi(1)
    wi(1)
    ci(1)
    mi(1)
    pi(1)
    //g1i(1) because changed unit produce way, now it's no use. consider later.
}
 
function fi(t){
    //food increase
    //alert('here')
    myElement = document.getElementById('f')
    //alert(myElement)
    if(myElement != null) {
        if (myElement.title>0) {
            {
            d = myElement.innerHTML.split("/");
            food = parseInt(d[0]); //food amount
            limit = parseInt(d[1]); //food limit
            inc = myElement.title/3600;
            if(food != limit)
                {
                setTimeout("fi(0)", 1/inc*1000);
                if(t == 0){myElement.innerHTML=food + 1 + "/" + limit;}
                }
            }
        }
    }
}

function wi(t){
    //wood increase
    myElement = document.getElementById('w');
    if(myElement != null)
    {
    if (myElement.title>0) {
    d = myElement.innerHTML.split("/");
    wood = parseInt(d[0]); //wood amount
    limit = parseInt(d[1]); //wood limit
    inc = myElement.title/3600;
    if(wood != limit)
    {
    setTimeout("wi(0)", 1/inc*1000);
    if(t == 0){myElement.innerHTML=wood + 1 + "/" + limit;}
    }
    }
    }
}

function ci(t){
    //clay increase
    myElement = document.getElementById('c');
    if(myElement != null)
    {
    if (myElement.title>0) {
    d = myElement.innerHTML.split("/");
    clay = parseInt(d[0]); //clay amount
    limit = parseInt(d[1]); //clay limit
    inc = myElement.title/3600;
    if(clay != limit)
    {
    setTimeout("ci(0)", 1/inc*1000);
    if(t == 0){myElement.innerHTML=clay + 1 + "/" + limit;}
    }
    }
    }
}

function mi(t){
    //mine increase
    myElement = document.getElementById('m');
    if(myElement != null)
    {
    if (myElement.title>0) {
    d = myElement.innerHTML.split("/");
    mine = parseInt(d[0]); //mine amount
    limit = parseInt(d[1]); //mine limit
    inc = myElement.title/3600;
    if(mine != limit)
    {
    setTimeout("mi(0)", 1/inc*1000);
    if(t == 0){myElement.innerHTML=mine + 1 + "/" + limit;}
    }
    }
    }
}

function pi(t){
    //pop increase
    myElement = document.getElementById('p');
    //alert(myElement.title)
    if(myElement != null)
    {
    d = myElement.innerHTML.split("/");
    pop = parseInt(d[0]); //population
    limit = parseInt(d[1]); //pop limit
    inc = myElement.title/3600;
    if(pop != limit)
    {
    setTimeout("pi(0)", 1/inc*1000);
    if(t == 0){myElement.innerHTML=pop + 1 + "/" + limit;}
    }
    }
}

function valid(num)
{
//alert("here");
if(isNaN(num) == true) {num = 0;}
document.form1.num1.value=num
//return num;
}

//*********ajax********test*******//

function creatXMLHttpRequest() {
	if(window.ActiveXObject) {
		this.xmlhttp = new ActiveXObject('Microsoft.XMLHTTP');
	} else if(window.XMLHttpRequest) {
		this.xmlhttp = new XMLHttpRequest();
	}
}

function startRequest(general_id) {
    //now try for soldier train!!!
    //alert("hi");
	//var queryString;
	//var num = document.getElementById('num1').value;
    var train_number = document.getElementById('soldier_number'+general_id).value;
    //alert (train_number)
    //var goods = document.getElementById('goods').value;
	//queryString = "domain=" + domain;
	creatXMLHttpRequest();
    //alert(train_number)
    //alert(xmlHttp);
	//xmlHttp.open("POST","?action=do","true");
    this.xmlhttp.open("POST","/military/train/",true);
    //alert("hi")
    //alert(train_number)
	this.xmlhttp.onreadystatechange = handleStateChange;
	this.xmlhttp.setRequestHeader("Content-Type","application/x-www-form-urlencoded;");
	this.xmlhttp.send("train_number="+train_number+"&general_id="+general_id);
}


function handleStateChange() {
	if(this.xmlhttp.readyState == 1) {
        //alert('tt4')
		//document.getElementById('result').style.cssText = "";
		//document.getElementById('result').innerText = "processing...";
	}
	if(this.xmlhttp.readyState == 4) {
        //alert('tt4')
        //alert(this.xmlhttp.status)
        //test
        //var fso, f;
        //fso = new ActiveXObject("Scripting.FileSystemObject");
        //根据路径创建文件；
        //f = fso.CreateTextFile("f:\\testfile.txt", true);
        //f.WriteLine(this.xmlhttp.responseText);
        //f.close();
        
        //alert(this.xmlhttp.responseText)
		if(this.xmlhttp.status == 200) {
            //alert('tt3')
			//document.getElementById('result').style.cssText = "";
			var allcon =  this.xmlhttp.responseText;
            //alert(allcon)
            eval("data = " + allcon);
            on_train(data);
            //parse
            //alert(data.body[1][1])
			//document.getElementById('result').innerHTML = allcon;
		}
	}
}

function on_train(data) {
    //ajax for soldier train.
    //hh1 = document.getElementById('h1').innerHTML
    //alert(data.body[1][1])
    if (data.body[0][0] == "error") {
        //alert(data.body[0][1])
        document.getElementById('train_error'+data.body[1][1]).innerHTML = data.body[0][1]
        }
    /*
    if (hh1 == "goods type") {
        if (data.body[0][0] == "ps_full") { //produce sequences are full. 5 now.
            document.getElementById('result').innerHTML = data.body[0][1]
        }
        else {
            //myTable = document.getElementsByTagName("TABLE");
            newRow=produce_table.insertRow()
            myNewCell1 = newRow.insertCell() 
            myNewCell2 = newRow.insertCell() 
            myNewCell1.innerHTML = data.body[5][1];
            myNewCell2.innerHTML = data.body[6][1];
        }
    }*/
    //minus_res(wood,clay,mine,food,silver) 
    //json_data = {'body':[('general_id',str(general_id)),('used_wood', cost_wood),('used_clay', cost_clay),('used_mine', cost_mine),('used_food', cost_food),('used_silver', cost_silver),('used_pop', train_number)]}
    else {
        minus_res(data.body[1][1],data.body[2][1],data.body[3][1],data.body[4][1],data.body[5][1],data.body[6][1])
        
        //tt=document.getElementById('in_traing'+data.body[0][1]).innerHTML
        //alert(tt)
        document.getElementById('in_traing'+data.body[0][1]).innerHTML = data.body[7][1]
        document.getElementById('train_error'+data.body[0][1]).innerHTML = ""
        document.getElementById('soldier_number'+data.body[0][1]).value=""
    }
    /*
    //minus resources and silver here. should judge what kind of resources at first.
    temp1 = parseInt(data.body[2][1]) * parseInt(data.body[6][1])
    //alert(temp)
    if (data.body[1][1]=="food") {minus_res(0,temp1,0,0,0)}
    if (data.body[1][1]=="wood") {minus_res(0,0,temp1,0,0)}
    if (data.body[1][1]=="mine") {minus_res(0,0,0,0,temp1)}
    if (data.body[1][1]=="clay") {minus_res(0,0,0,temp1,0)}
    
    if (data.body[3][1] != "None") { //if exists 2nd resources
        //alert("here")
        temp1 = parseInt(data.body[4][1]) * parseInt(data.body[6][1])
        if (data.body[3][1]=="wood") {minus_res(0,0,temp1,0,0)}
        if (data.body[3][1]=="food") {minus_res(0,temp1,0,0,0)}
        if (data.body[3][1]=="mine") {minus_res(0,0,0,0,temp1)}
        if (data.body[3][1]=="clay") {minus_res(0,0,0,temp1,0)}
    }
    
    //minus silver
    temp1 = parseInt(data.body[7][1]) * parseInt(data.body[6][1])
    minus_res(temp1,0,0,0,0)
    //if (data.body[1][1]=="silver") {minus_res(0,0,0,0,temp1)} */
    
}

function g1i(t){
    //function to deal with goods' increase, according to the unit's produce sequences.
    //for all unit, check if there's produce seq. exists or not...
    for ( var i = 1; i < MAX_BUILDING_NUMBER; i++ ) { //because unit_type is bounded to building.
        up = document.getElementById('up'+i+'_'+1) 
        //unit produce, from the first produce seq. of the unit, so it's "1"
        
        if (up!=null) {
            //parse the up data, now it's like: 
            //<li id=up21_1 style="display:none">3.333/1/11053/3/2007,04,08,17,57,12</li>
            //they are: produce_speed/unit_seq/goods_quantity/goods.id/last_goods_finish_time
            u = up.innerHTML.split("/"); 
            var temp = u[2] - Math.floor(u[2]);
            var time_now = new Date()

            uu = u[4].split(",");
            //u[4] is like 2007,04,08,02,46,12
            
            var time_lgf = new Date()
            time_lgf.setYear(uu[0])
            time_lgf.setMonth(uu[1]-1)
            time_lgf.setDate(uu[2])
            time_lgf.setHours(uu[3],uu[4],uu[5])
            
            timed = time_now.getTime() - Date.parse(time_lgf)  
            
            setTimeout("good_inc('" + parseInt(u[3]) + "','" + i + "','" + 1 + "','" + 1 +"')", 3600000/u[0]-timed)            
            //alert(3600000/u[0]-timed)
            //setTimeout("good_inc('" + parseInt(u[3]) + "','" + i + "','" + 1 + "','" + 0 +"')", 3600000*temp/u[0])
        }
    }
}

function good_inc(gid,uid,seq,t) {
    //sub-function to deal with goods' increase, according to the unit's produce sequences.
    //alert(gid)
    goods=document.getElementById('g'+gid);
    up = document.getElementById('up'+uid+'_'+seq);
    if (up!=null) {
        u = up.innerHTML.split("/");

        //else {
            if (parseInt(u[2])==0) { //this produce seq. completed, start to deal with next one. note:still same unit.
                var next_seq = parseInt(seq)+1
                //alert(next_seq)
                up = document.getElementById('up'+uid+'_'+next_seq);
                if (up != null) {
                    //alert("here")
                    //setTimeout("good_inc('" + gid + "','" + uid + "','" + next_seq + "','" + 1 +"')", 3600000/u[0])
                    setTimeout("good_inc('" + gid + "','" + uid + "','" + next_seq + "','" + 1 +"')", 0)
                }
            }
            else { //still the same produce sequence.
                goods.innerHTML = parseInt(goods.innerHTML) + 1
                //alert("here")
                up.innerHTML = u[0]+"/"+ u[1]+"/"+ (parseInt(u[2])-1) +"/"+gid;
                setTimeout("good_inc('" + gid + "','" + uid + "','"+ seq + "','" + 1 +"')", 3600000/u[0])
            }
        //}
    }
    
}

function minus_res(wood,clay,mine,food,silver,pop) {
    //minus resources. will be used when buildings update, or city produce sequences created.
    //maybe others event will call this too?
    vs = vs - silver
    vf = vf - food
    vw = vw - wood
    vc = vc - clay
    vm = vm - mine
    vp = vp - pop
    s.innerHTML = vs + "/" + vsl
    f.innerHTML = vf + "/" + vfl
    w.innerHTML = vw + "/" + vrl
    c.innerHTML = vc + "/" + vrl
    m.innerHTML = vm + "/" + vrl
    p.innerHTML = vp + "/" + vpl
}

function event_timer(time_remain,counter) {
    //timer for all events, now in testing!
    //note:because js count month from 0 to 11, so in template, use format as: |date:"Y,m-1,d,H,i,s"
    //var upd_st = new Date(start_time)
    //var upd_et_org = new Date(end_time)
    //alert("here")
    //test et=new Date().settime(upd_et.gettime()+(-480-upd_et.getTimezoneOffset())*60*1000*1000)
    //alert(end_time-server_now)
    //time_dif = end_time-server_now
    //var et=new Date()
    //alert(upd_et_org.getTimezoneOffset())
    //alert(upd_et_org.getTime())
    //a1=(-360-upd_et_org.getTimezoneOffset())*60*60*1000
    //alert(time_remain)
    //var et1=et.setTime(upd_et_org.getTime()+(-480-upd_et_org.getTimezoneOffset())*60*1000*1000)
    //alert(time_compen)
    //var upd_et1 = et.setTime(upd_et_org.getTime()+time_compen)
    //upd_et=new Date(upd_et1)
    //alert(upd_et)
    
    //var now_time = new Date()
    //var remain_time = (upd_et - now_time)/1000
    //var remain_time = (end_time - server_now)/1000
    //alert(time_remain)
    
    rt = parseInt(time_remain) + 5 //compensation for server dealing time...try
    eventid=document.getElementById('event_time_remain'+counter);
    //alert(rt)
    if (rt == 0) 
    {
       window.location.reload();
    }
    else 
    {  
       //event_bldup.innerHTML = "<br>building is updating, started at " + upd_st.getHours() + ":" + upd_st.getMinutes() + ":" + upd_st.getSeconds() + ", end at " + upd_et + ", time remaining: " + rt + "seconds";
       //eventid.innerHTML = rt;
       eventid.innerHTML = time_format(rt);
       //var et2=new Date()
       //var upd_et2 = et2.setTime(upd_et_org.getTime()-time_compen)
       //upd_et=new Date(upd_et2)
       //alert(upd_et)
       //alert(time_remain)
       time_remain = time_remain - 1
       //alert(time_remain)
       setTimeout("event_timer('" + time_remain + "','" + counter + "')",1000) 
       //setTimeout("event_timer('" + upd_st + "', '" + upd_et_org + "','" + counter + "')",1000) 
    }
}

function time_format(s) {
//from seconds to hh:mm:ss format
if(s > -1){
    //alert(s)
    hour = Math.floor(s/3600);
    //alert(hour)
    min = Math.floor(s/60) % 60;
    sec = s % 60; 
    t = hour + ":";
    if(min < 10){t += "0";}
        t += min + ":";
    if(sec < 10){t += "0";}
        t += sec;}
else
    {t = "0:00:0x";}
return t;
}

function live_combat_timer(time_remain) {
    //timer for live combat, now in testing!
    //note:because js count month from 0 to 11, so in template, use format as: |date:"Y,m-1,d,H,i,s"
    //var upd_st = new Date(start_time)
    //var upd_et = new Date(end_time)
    
    //var now_time = new Date()
    //var remain_time = (upd_et - now_time)/1000
    
    var rt = parseInt(time_remain) + 5 //compensation for server dealing time...try
    //var rt = parseInt(remain_time)
    
    eventid=document.getElementById('next_round_time_remain'); 
    //alert(rt)
    if (rt == 0) 
    {
       window.location.reload();
    }
    else 
    {  
       //event_bldup.innerHTML = "<br>building is updating, started at " + upd_st.getHours() + ":" + upd_st.getMinutes() + ":" + upd_st.getSeconds() + ", end at " + upd_et + ", time remaining: " + rt + "seconds";
       //eventid.innerHTML = rt;
       eventid.innerHTML = time_format(rt);
       time_remain = time_remain - 1
       setTimeout("live_combat_timer('" + time_remain + "')",1000) 
    }
}

function skill_add(obj,sid,skillid){
//swordsman adds skill point. use ajax...maybe.
obj.href = "/military/swordsman_as/?sid=" + sid +"&skillid=" + skillid;
obj.click();
}