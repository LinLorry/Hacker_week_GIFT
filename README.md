## url:http://120.78.94.18:5000/<一级类别名>/
# method="GET"
'''
return
{class_1:{
	name:口红
	j_standard:{
		first:第一个划分依据,
		second:第二个划分依据,
		.......
		}
	（X）_title:该类X品的大标题，
	（X）_preface:该类X品的引言，
	（X有top,low,medium)
	},
class_2:......
......}
'''

------------------------------------------------
## url:http://120.78.94.18:5000/<一级类别名>/<二级类别名>
# method="GET"
'''
return:
{
"j_standard":"该二级类的划分标准",
"products":{
	"level_1":"下级产品",
	......
	"level_9":"上级产品",
	"level_low":"随机下级产品",
	"level_middle":"随机中级产品",
	"level_top":"随机上级产品",
	}
}
'''
--------------------------------------------
## http://120.78.94.18:5000/<一级类别名>/<二级类别名><产品名>
#method="GET"
'''
return
{
"name":"名字",
"level":"等级",
"price":"价格",
"title":"小标题",
"commentaries":"该产品的介绍与评价"
}
'''
--------------------------------------------
## http://120.78.94.18:5000/images/
# method="POST"
'''
POST
{
"class_name":"二级类别名",
"name":"产品名"
}
return
{
"image_1":"图片一地址",
"image_2":"图片二地址",
"image_3":"图片三地址"
}
'''
