import pypinyin
from .models import VehicleProvince
from .models import AcquisitionVarieties,GBCornInformations
from django.db import connection
from django.conf import settings
import pypinyin
import base64,sys,os
#  车辆所属省份
def vehicle_default():
    VLPLATE=[
        [1, '110000', '北京市', '京', '', '北京市', 'A'],
        [7, '120000', '天津市', '津', '', '天津市', 'A'],
        [11, '130000', '河北省', '冀', '130100', '石家庄市', 'A' ],
        [12, '130000', '河北省', '冀', '130200', '唐山市', 'B' ],
        [13, '130000', '河北省', '冀', '130300', '秦皇岛市', 'C' ],
        [14, '130000', '河北省', '冀', '130400', '邯郸市', 'D' ],
        [15, '130000', '河北省', '冀', '130500', '邢台市', 'E' ],
        [16, '130000', '河北省', '冀', '130600', '保定市', 'F' ],
        [17, '130000', '河北省', '冀', '130700', '张家口市', 'G' ],
        [18, '130000', '河北省', '冀', '130800', '承德市', 'H' ],
        [19, '130000', '河北省', '冀', '130900', '沧州市', 'J' ],
        [21, '130000', '河北省', '冀', '131000', '廊坊市', 'R' ],
        [22, '130000', '河北省', '冀', '131100', '衡水市', 'T' ],
        [23, '140000', '山西省', '晋', '140100', '太原市', 'A' ],
        [24, '140000', '山西省', '晋', '140200', '大同市', 'B' ],
        [25, '140000', '山西省', '晋', '140300', '阳泉市', 'C' ],
        [26, '140000', '山西省', '晋', '140400', '长治市', 'D' ],
        [27, '140000', '山西省', '晋', '140500', '晋城市', 'E' ],
        [28, '140000', '山西省', '晋', '140600', '朔州市', 'F' ],
        [29, '140000', '山西省', '晋', '', '雁北市', 'G' ],
        [30, '140000', '山西省', '晋', '140700', '晋中市', 'K' ],
        [31, '140000', '山西省', '晋', '140800', '运城市', 'M' ],
        [32, '140000', '山西省', '晋', '140900', '忻州市', 'H' ],
        [33, '140000', '山西省', '晋', '141000', '临汾市', 'L' ],
        [34, '140000', '山西省', '晋', '141100', '吕梁市', 'J' ],
        [35, '150000', '内蒙古', '蒙', '150100', '呼和浩特市', 'A' ],
        [36, '150000', '内蒙古', '蒙', '150200', '包头市', 'B' ],
        [37, '150000', '内蒙古', '蒙', '150300', '乌海市', 'C' ],
        [38, '150000', '内蒙古', '蒙', '150400', '赤峰市', 'D' ],
        [39, '150000', '内蒙古', '蒙', '150500', '通辽市', 'G' ],
        [40, '150000', '内蒙古', '蒙', '150600', '鄂尔多斯市', 'K' ],
        [41, '150000', '内蒙古', '蒙', '150700', '呼伦贝尔市', 'E' ],
        [42, '150000', '内蒙古', '蒙', '150800', '巴彦淖尔市', 'L' ],
        [43, '150000', '内蒙古', '蒙', '150900', '乌兰察布市', 'J' ],
        [44, '150000', '内蒙古', '蒙', '152200', '兴安', 'F' ],
        [45, '150000', '内蒙古', '蒙', '152500', '锡林郭勒', 'H' ],
        [46, '150000', '内蒙古', '蒙', '152900', '阿拉善', 'M' ],
        [47, '210000', '辽宁省', '辽', '210100', '沈阳市', 'A' ],
        [48, '210000', '辽宁省', '辽', '210200', '大连市', 'B' ],
        [49, '210000', '辽宁省', '辽', '210300', '鞍山市', 'C' ],
        [50, '210000', '辽宁省', '辽', '210400', '抚顺市', 'D' ],
        [51, '210000', '辽宁省', '辽', '210500', '本溪市', 'E' ],
        [52, '210000', '辽宁省', '辽', '210600', '丹东市', 'F' ],
        [53, '210000', '辽宁省', '辽', '210700', '锦州市', 'G' ],
        [54, '210000', '辽宁省', '辽', '210800', '营口市', 'H' ],
        [55, '210000', '辽宁省', '辽', '210900', '阜新市', 'J' ],
        [56, '210000', '辽宁省', '辽', '211000', '辽阳市', 'K' ],
        [57, '210000', '辽宁省', '辽', '211100', '盘锦市', 'L' ],
        [58, '210000', '辽宁省', '辽', '211200', '铁岭市', 'M' ],
        [59, '210000', '辽宁省', '辽', '211300', '朝阳市', 'N' ],
        [60, '210000', '辽宁省', '辽', '211400', '葫芦岛市', 'P' ],
        [61, '220000', '吉林省', '吉', '220100', '长春市', 'A' ],
        [62, '220000', '吉林省', '吉', '220200', '吉林市', 'B' ],
        [63, '220000', '吉林省', '吉', '220300', '四平市', 'C' ],
        [64, '220000', '吉林省', '吉', '220400', '辽源市', 'D' ],
        [65, '220000', '吉林省', '吉', '220500', '通化市', 'E' ],
        [66, '220000', '吉林省', '吉', '220600', '白山市', 'F' ],
        [67, '220000', '吉林省', '吉', '220700', '松原市', 'J' ],
        [68, '220000', '吉林省', '吉', '220800', '白城市', 'G' ],
        [69, '220000', '吉林省', '吉', '222400', '延边州', 'H' ],
        [70, '230000', '黑龙江省', '黑', '230100', '哈尔滨市', 'A' ],
        [71, '230000', '黑龙江省', '黑', '230200', '齐齐哈尔市', 'B' ],
        [72, '230000', '黑龙江省', '黑', '230300', '鸡西市', 'G' ],
        [73, '230000', '黑龙江省', '黑', '230400', '鹤岗市', 'H' ],
        [74, '230000', '黑龙江省', '黑', '230500', '双鸭山市', 'J' ],
        [75, '230000', '黑龙江省', '黑', '230600', '大庆市', 'E' ],
        [76, '230000', '黑龙江省', '黑', '230700', '伊春市', 'F' ],
        [77, '230000', '黑龙江省', '黑', '230800', '佳木斯市', 'D' ],
        [78, '230000', '黑龙江省', '黑', '230900', '七台河市', 'K' ],
        [79, '230000', '黑龙江省', '黑', '231000', '牡丹江市', 'C' ],
        [80, '230000', '黑龙江省', '黑', '231100', '黑河市', 'N' ],
        [81, '230000', '黑龙江省', '黑', '231200', '绥化市', 'M' ],
        [82, '230000', '黑龙江省', '黑', '', '松花江市', 'L' ],
        [83, '230000', '黑龙江省', '黑', '', '农恳市', 'R' ],
        [84, '230000', '黑龙江省', '黑', '232700', '大兴安岭区', 'P' ],
        [86, '320000', '江苏省', '苏', '320100', '南京市', 'A' ],
        [87, '320000', '江苏省', '苏', '320200', '无锡市', 'B' ],
        [88, '320000', '江苏省', '苏', '320300', '徐州市', 'C' ],
        [89, '320000', '江苏省', '苏', '320400', '常州市', 'D' ],
        [90, '320000', '江苏省', '苏', '320500', '苏州市', 'E' ],
        [91, '320000', '江苏省', '苏', '320600', '南通市', 'F' ],
        [92, '320000', '江苏省', '苏', '320700', '连云港市', 'G' ],
        [93, '320000', '江苏省', '苏', '320800', '淮安市', 'H' ],
        [94, '320000', '江苏省', '苏', '320900', '盐城市', 'J' ],
        [95, '320000', '江苏省', '苏', '321000', '扬州市', 'K' ],
        [96, '320000', '江苏省', '苏', '321100', '镇江市', 'L' ],
        [97, '320000', '江苏省', '苏', '321200', '泰州市', 'M' ],
        [98, '320000', '江苏省', '苏', '321300', '宿迁市', 'N' ],
        [99, '330000', '浙江省', '浙', '330100', '杭州市', 'A' ],
        [100, '330000', '浙江省', '浙', '330200', '宁波市', 'B' ],
        [101, '330000', '浙江省', '浙', '330300', '温州市', 'C' ],
        [102, '330000', '浙江省', '浙', '330400', '嘉兴市', 'F' ],
        [103, '330000', '浙江省', '浙', '330500', '湖州市', 'E' ],
        [104, '330000', '浙江省', '浙', '330600', '绍兴市', 'D' ],
        [105, '330000', '浙江省', '浙', '330700', '金华市', 'G' ],
        [106, '330000', '浙江省', '浙', '330800', '衢州市', 'H' ],
        [107, '330000', '浙江省', '浙', '330900', '舟山市', 'L' ],
        [108, '330000', '浙江省', '浙', '331000', '台州市', 'J' ],
        [109, '330000', '浙江省', '浙', '331100', '丽水市', 'K' ],
        [110, '340000', '安徽省', '皖', '340100', '合肥市', 'A' ],
        [111, '340000', '安徽省', '皖', '340200', '芜湖市', 'B' ],
        [112, '340000', '安徽省', '皖', '340300', '蚌埠市', 'C' ],
        [113, '340000', '安徽省', '皖', '340400', '淮南市', 'D' ],
        [114, '340000', '安徽省', '皖', '340500', '马鞍山市', 'E' ],
        [115, '340000', '安徽省', '皖', '340600', '淮北市', 'F' ],
        [116, '340000', '安徽省', '皖', '340700', '铜陵市', 'G' ],
        [117, '340000', '安徽省', '皖', '340800', '安庆市', 'H' ],
        [118, '340000', '安徽省', '皖', '341000', '黄山市', 'J' ],
        [119, '340000', '安徽省', '皖', '341100', '滁州市', 'M' ],
        [120, '340000', '安徽省', '皖', '341200', '阜阳市', 'K' ],
        [121, '340000', '安徽省', '皖', '341300', '宿州市', 'L' ],
        [122, '340000', '安徽省', '皖', '341400', '巢湖市', 'Q' ],
        [123, '340000', '安徽省', '皖', '341500', '六安市', 'N' ],
        [124, '340000', '安徽省', '皖', '341600', '亳州市', 'S' ],
        [125, '340000', '安徽省', '皖', '341700', '池州市', 'R' ],
        [126, '340000', '安徽省', '皖', '341800', '宣城市', 'P' ],
        [127, '350000', '福建省', '闽', '350100', '福州市', 'A' ],
        [128, '350000', '福建省', '闽', '350200', '厦门市', 'D' ],
        [129, '350000', '福建省', '闽', '350300', '莆田市', 'B' ],
        [130, '350000', '福建省', '闽', '350400', '三明市', 'G' ],
        [131, '350000', '福建省', '闽', '350500', '泉州市', 'C' ],
        [132, '350000', '福建省', '闽', '350600', '漳州市', 'E' ],
        [133, '350000', '福建省', '闽', '350700', '南平市', 'H' ],
        [134, '350000', '福建省', '闽', '350800', '龙岩市', 'F' ],
        [135, '350000', '福建省', '闽', '350900', '宁德市', 'J' ],
        [136, '350000', '福建省', '闽', '', '省直系统', 'K' ],
        [137, '360000', '江西省', '赣', '360100', '南昌市', 'A' ],
        [138, '360000', '江西省', '赣', '360100', '南昌市市', 'M' ],
        [139, '360000', '江西省', '赣', '360200', '景德镇市', 'H' ],
        [140, '360000', '江西省', '赣', '360300', '萍乡市', 'J' ],
        [141, '360000', '江西省', '赣', '360400', '九江市', 'G' ],
        [142, '360000', '江西省', '赣', '360500', '新余市', 'K' ],
        [143, '360000', '江西省', '赣', '360600', '鹰潭市', 'L' ],
        [144, '360000', '江西省', '赣', '360700', '赣州市', 'B' ],
        [145, '360000', '江西省', '赣', '360800', '吉安市', 'D' ],
        [146, '360000', '江西省', '赣', '360900', '宜春市', 'C' ],
        [147, '360000', '江西省', '赣', '361000', '抚州市', 'F' ],
        [148, '360000', '江西省', '赣', '361100', '上饶市', 'E' ],
        [149, '370000', '山东省', '鲁', '370100', '济南市', 'A' ],
        [150, '370000', '山东省', '鲁', '370200', '青岛市', 'B' ],
        [152, '370000', '山东省', '鲁', '370300', '淄博市', 'C' ],
        [153, '370000', '山东省', '鲁', '370400', '枣庄市', 'D' ],
        [154, '370000', '山东省', '鲁', '370500', '东营市', 'E' ],
        [155, '370000', '山东省', '鲁', '370600', '烟台市', 'F' ],
        [156, '370000', '山东省', '鲁', '370700', '潍坊市', 'G' ],
        [157, '370000', '山东省', '鲁', '370700', '潍坊市市', 'V' ],
        [158, '370000', '山东省', '鲁', '370800', '济宁市', 'H' ],
        [159, '370000', '山东省', '鲁', '370900', '泰安市', 'J' ],
        [160, '370000', '山东省', '鲁', '371000', '威海市', 'K' ],
        [161, '370000', '山东省', '鲁', '371100', '日照市', 'L' ],
        [162, '370000', '山东省', '鲁', '371200', '莱芜市', 'S' ],
        [163, '370000', '山东省', '鲁', '371300', '临沂市', 'Q' ],
        [164, '370000', '山东省', '鲁', '371400', '德州市', 'N' ],
        [165, '370000', '山东省', '鲁', '371500', '聊城市', 'P' ],
        [166, '370000', '山东省', '鲁', '371600', '滨州市', 'M' ],
        [167, '370000', '山东省', '鲁', '371700', '菏泽市', 'R' ],
        [168, '410000', '河南省', '豫', '410100', '郑州市', 'A' ],
        [169, '410000', '河南省', '豫', '410200', '开封市', 'B' ],
        [170, '410000', '河南省', '豫', '410300', '洛阳市', 'C' ],
        [171, '410000', '河南省', '豫', '410400', '平顶山市', 'D' ],
        [172, '410000', '河南省', '豫', '410500', '安阳市', 'E' ],
        [173, '410000', '河南省', '豫', '410600', '鹤壁市', 'F' ],
        [174, '410000', '河南省', '豫', '410700', '新乡市', 'G' ],
        [175, '410000', '河南省', '豫', '410800', '焦作市', 'H' ],
        [176, '410000', '河南省', '豫', '410900', '濮阳市', 'J' ],
        [177, '410000', '河南省', '豫', '411000', '许昌市', 'K' ],
        [178, '410000', '河南省', '豫', '411100', '漯河市', 'L' ],
        [179, '410000', '河南省', '豫', '411200', '三门峡市', 'M' ],
        [180, '410000', '河南省', '豫', '411300', '南阳市', 'R' ],
        [181, '410000', '河南省', '豫', '411400', '商丘市', 'N' ],
        [182, '410000', '河南省', '豫', '411500', '信阳市', 'S' ],
        [183, '410000', '河南省', '豫', '411600', '周口市', 'P' ],
        [184, '410000', '河南省', '豫', '411700', '驻马店市', 'Q' ],
        [185, '410000', '河南省', '豫', '411800', '济源市', 'U' ],
        [186, '420000', '湖北省', '鄂', '420100', '武汉市', 'A' ],
        [187, '420000', '湖北省', '鄂', '420200', '黄石市', 'B' ],
        [188, '420000', '湖北省', '鄂', '420300', '十堰市', 'C' ],
        [189, '420000', '湖北省', '鄂', '420500', '宜昌市', 'E' ],
        [190, '420000', '湖北省', '鄂', '420600', '襄阳市', 'F' ],
        [191, '420000', '湖北省', '鄂', '420700', '鄂州市', 'G' ],
        [192, '420000', '湖北省', '鄂', '420800', '荆门市', 'H' ],
        [193, '420000', '湖北省', '鄂', '420900', '孝感市', 'K' ],
        [194, '420000', '湖北省', '鄂', '421000', '荆州市', 'D' ],
        [195, '420000', '湖北省', '鄂', '421100', '黄冈市', 'J' ],
        [196, '420000', '湖北省', '鄂', '421200', '咸宁市', 'L' ],
        [197, '420000', '湖北省', '鄂', '421300', '随州市', 'S' ],
        [198, '420000', '湖北省', '鄂', '421400', '神农架区', 'P' ],
        [199, '420000', '湖北省', '鄂', '421500', '天门市', 'R' ],
        [200, '420000', '湖北省', '鄂', '421600', '潜江市', 'N' ],
        [201, '420000', '湖北省', '鄂', '421700', '仙桃市', 'M' ],
        [202, '420000', '湖北省', '鄂', '422800', '恩施州', 'Q' ],
        [203, '430000', '湖南省', '湘', '430100', '长沙市', 'A' ],
        [204, '430000', '湖南省', '湘', '430200', '株洲市', 'B' ],
        [205, '430000', '湖南省', '湘', '430300', '湘潭市', 'C' ],
        [206, '430000', '湖南省', '湘', '430400', '衡阳市', 'D' ],
        [207, '430000', '湖南省', '湘', '430500', '邵阳市', 'E' ],
        [208, '430000', '湖南省', '湘', '430600', '岳阳市', 'F' ],
        [209, '430000', '湖南省', '湘', '430700', '常德市', 'J' ],
        [210, '430000', '湖南省', '湘', '430800', '张家界市', 'G' ],
        [211, '430000', '湖南省', '湘', '430900', '益阳市', 'H' ],
        [212, '430000', '湖南省', '湘', '431000', '郴州市', 'L' ],
        [213, '430000', '湖南省', '湘', '431100', '永州市', 'M' ],
        [214, '430000', '湖南省', '湘', '431200', '怀化市', 'N' ],
        [215, '430000', '湖南省', '湘', '431300', '娄底市', 'K' ],
        [216, '430000', '湖南省', '湘', '433100', '湘西州', 'U' ],
        [217, '440000', '广东省', '粤', '440100', '广州市', 'A' ],
        [218, '440000', '广东省', '粤', '440200', '韶关市', 'F' ],
        [219, '440000', '广东省', '粤', '440300', '深圳市', 'B' ],
        [220, '440000', '广东省', '粤', '440400', '珠海市', 'C' ],
        [221, '440000', '广东省', '粤', '440500', '汕头市', 'D' ],
        [222, '440000', '广东省', '粤', '440600', '佛山市', 'E' ],
        [223, '440000', '广东省', '粤', '', '顺德市', 'X' ],
        [225, '440000', '广东省', '粤', '440700', '江门市', 'J' ],
        [226, '440000', '广东省', '粤', '440800', '湛江市', 'G' ],
        [227, '440000', '广东省', '粤', '440900', '茂名市', 'K' ],
        [228, '440000', '广东省', '粤', '441200', '肇庆市', 'H' ],
        [229, '440000', '广东省', '粤', '441300', '惠州市', 'L' ],
        [230, '440000', '广东省', '粤', '441400', '梅州市', 'M' ],
        [231, '440000', '广东省', '粤', '441500', '汕尾市', 'N' ],
        [232, '440000', '广东省', '粤', '441600', '河源市', 'P' ],
        [233, '440000', '广东省', '粤', '441700', '阳江市', 'Q' ],
        [234, '440000', '广东省', '粤', '441800', '清远市', 'R' ],
        [235, '440000', '广东省', '粤', '441900', '东莞市', 'S' ],
        [236, '440000', '广东省', '粤', '442000', '中山市', 'T' ],
        [237, '440000', '广东省', '粤', '445100', '潮州市', 'U' ],
        [238, '440000', '广东省', '粤', '445200', '揭阳市', 'V' ],
        [239, '440000', '广东省', '粤', '445300', '云浮市', 'W' ],
        [241, '450000', '广西', '桂', '450100', '南宁市', 'A' ],
        [242, '450000', '广西', '桂', '450200', '柳州市', 'B' ],
        [243, '450000', '广西', '桂', '450300', '桂林市', 'C' ],
        [244, '450000', '广西', '桂', '450400', '梧州市', 'D' ],
        [245, '450000', '广西', '桂', '450500', '北海市', 'E' ],
        [246, '450000', '广西', '桂', '450600', '防城港市', 'P' ],
        [247, '450000', '广西', '桂', '450700', '钦州市', 'N' ],
        [248, '450000', '广西', '桂', '450800', '贵港市', 'R' ],
        [249, '450000', '广西', '桂', '450900', '玉林市', 'K' ],
        [250, '450000', '广西', '桂', '451000', '百色市', 'L' ],
        [251, '450000', '广西', '桂', '451100', '贺州市', 'J' ],
        [252, '450000', '广西', '桂', '451200', '河池市', 'M' ],
        [253, '450000', '广西', '桂', '451300', '来宾市', 'G' ],
        [254, '450000', '广西', '桂', '451400', '崇左市', 'F' ],
        [255, '460000', '海南省', '琼', '460100', '海口市', 'A' ],
        [256, '460000', '海南省', '琼', '460200', '三亚市', 'B' ],
        [257, '460000', '海南省', '琼', '', '洋浦开发区', 'E' ],
        [258, '460000', '海南省', '琼', '460500', '五指山市', 'D' ],
        [259, '460000', '海南省', '琼', '460600', '琼海市', 'C' ],
        [260, '500000', '重庆市', '渝', '500100', '重庆市', 'A' ],
        [262, '500000', '重庆市', '渝', '', '永川区市', 'C' ],
        [263, '500000', '重庆市', '渝', '', '万州区', 'F' ],
        [264, '500000', '重庆市', '渝', '', '涪陵区', 'G' ],
        [265, '500000', '重庆市', '渝', '', '黔江区', 'H' ],
        [266, '510000', '四川省', '川', '510100', '成都市', 'A' ],
        [267, '510000', '四川省', '川', '510300', '自贡市', 'C' ],
        [268, '510000', '四川省', '川', '510400', '攀枝花市', 'D' ],
        [269, '510000', '四川省', '川', '510500', '泸州市', 'E' ],
        [270, '510000', '四川省', '川', '510600', '德阳市', 'F' ],
        [271, '510000', '四川省', '川', '510700', '绵阳市', 'B' ],
        [272, '510000', '四川省', '川', '510800', '广元市', 'H' ],
        [273, '510000', '四川省', '川', '510900', '遂宁市', 'J' ],
        [274, '510000', '四川省', '川', '511000', '内江市', 'K' ],
        [275, '510000', '四川省', '川', '511100', '乐山市', 'L' ],
        [276, '510000', '四川省', '川', '511300', '南充市', 'R' ],
        [277, '510000', '四川省', '川', '511400', '眉山市', 'Z' ],
        [278, '510000', '四川省', '川', '511500', '宜宾市', 'Q' ],
        [279, '510000', '四川省', '川', '511600', '广安市', 'X' ],
        [280, '510000', '四川省', '川', '511700', '达川市', 'S' ],
        [281, '510000', '四川省', '川', '511800', '雅安市', 'T' ],
        [282, '510000', '四川省', '川', '511900', '巴中市', 'Y' ],
        [283, '510000', '四川省', '川', '512000', '资阳市', 'M' ],
        [286, '510000', '四川省', '川', '513200', '阿坝州', 'U' ],
        [287, '510000', '四川省', '川', '513300', '甘孜州', 'V' ],
        [288, '510000', '四川省', '川', '513400', '凉山州', 'W' ],
        [289, '520000', '贵州省', '贵', '520100', '贵阳市', 'A' ],
        [290, '520000', '贵州省', '贵', '520200', '六盘水市', 'B' ],
        [291, '520000', '贵州省', '贵', '520300', '遵义市', 'C' ],
        [292, '520000', '贵州省', '贵', '520400', '安顺市', 'G' ],
        [293, '520000', '贵州省', '贵', '522200', '铜仁地区', 'D' ],
        [294, '520000', '贵州省', '贵', '522300', '黔西南州', 'E' ],
        [295, '520000', '贵州省', '贵', '522400', '毕节地区', 'F' ],
        [296, '520000', '贵州省', '贵', '522600', '黔东南州', 'H' ],
        [297, '520000', '贵州省', '贵', '522700', '黔南州', 'J' ],
        [298, '530000', '云南省', '云', '530100', '昆明市', 'A' ],
        [299, '530000', '云南省', '云', '', '普洱市', 'J' ],
        [300, '530000', '云南省', '云', '530300', '曲靖市', 'D' ],
        [301, '530000', '云南省', '云', '530400', '玉溪市', 'F' ],
        [302, '530000', '云南省', '云', '530500', '保山市', 'M' ],
        [303, '530000', '云南省', '云', '530600', '昭通市', 'C' ],
        [304, '530000', '云南省', '云', '530700', '丽江市', 'P' ],
        [305, '530000', '云南省', '云', '530900', '临沧市', 'S' ],
        [306, '530000', '云南省', '云', '532300', '楚雄州', 'E' ],
        [307, '530000', '云南省', '云', '532500', '红河州', 'G' ],
        [308, '530000', '云南省', '云', '532600', '文山州', 'H' ],
        [309, '530000', '云南省', '云', '532800', '西双版纳州', 'K' ],
        [310, '530000', '云南省', '云', '532900', '大理州', 'L' ],
        [311, '530000', '云南省', '云', '533100', '德宏州', 'N' ],
        [312, '530000', '云南省', '云', '533300', '怒江州', 'Q' ],
        [313, '530000', '云南省', '云', '533400', '迪庆州', 'R' ],
        [314, '540000', '西藏', '藏', '540100', '拉萨市', 'A' ],
        [315, '540000', '西藏', '藏', '542100', '昌都地区', 'B' ],
        [316, '540000', '西藏', '藏', '542200', '山南地区', 'C' ],
        [317, '540000', '西藏', '藏', '542300', '日喀则地区', 'D' ],
        [318, '540000', '西藏', '藏', '542400', '那曲地区', 'E' ],
        [319, '540000', '西藏', '藏', '542500', '阿里地区', 'F' ],
        [320, '540000', '西藏', '藏', '542600', '林芝地区', 'G' ],
        [321, '610000', '陕西省', '陕', '610100', '西安市', 'A' ],
        [322, '610000', '陕西省', '陕', '610200', '铜川市', 'B' ],
        [323, '610000', '陕西省', '陕', '610300', '宝鸡市', 'C' ],
        [324, '610000', '陕西省', '陕', '610400', '咸阳市', 'D' ],
        [325, '610000', '陕西省', '陕', '610500', '渭南市', 'E' ],
        [326, '610000', '陕西省', '陕', '610600', '延安市', 'J' ],
        [327, '610000', '陕西省', '陕', '610700', '汉中市', 'F' ],
        [328, '610000', '陕西省', '陕', '610800', '榆林市', 'K' ],
        [329, '610000', '陕西省', '陕', '610900', '安康市', 'G' ],
        [330, '610000', '陕西省', '陕', '611000', '商洛市', 'H' ],
        [332, '620000', '甘肃省', '甘', '620100', '兰州市', 'A' ],
        [333, '620000', '甘肃省', '甘', '620200', '嘉峪关市', 'B' ],
        [334, '620000', '甘肃省', '甘', '620300', '金昌市', 'C' ],
        [335, '620000', '甘肃省', '甘', '620400', '白银市', 'D' ],
        [336, '620000', '甘肃省', '甘', '620500', '天水市', 'E' ],
        [337, '620000', '甘肃省', '甘', '620600', '武威市', 'H' ],
        [338, '620000', '甘肃省', '甘', '620700', '张掖市', 'G' ],
        [339, '620000', '甘肃省', '甘', '620800', '平凉市', 'L' ],
        [340, '620000', '甘肃省', '甘', '620900', '酒泉市', 'F' ],
        [341, '620000', '甘肃省', '甘', '621000', '庆阳市', 'M' ],
        [342, '620000', '甘肃省', '甘', '621100', '定西市', 'J' ],
        [343, '620000', '甘肃省', '甘', '621200', '陇南市', 'K' ],
        [344, '620000', '甘肃省', '甘', '622900', '临夏州', 'N' ],
        [345, '620000', '甘肃省', '甘', '623000', '甘南州', 'P' ],
        [346, '630000', '青海省', '青', '630100', '西宁市', 'A' ],
        [347, '630000', '青海省', '青', '630300', '海南州', 'H' ],
        [348, '630000', '青海省', '青', '632100', '海东地区', 'B' ],
        [349, '630000', '青海省', '青', '632200', '海北州', 'C' ],
        [350, '630000', '青海省', '青', '632300', '黄南州', 'D' ],
        [352, '630000', '青海省', '青', '632600', '果洛州', 'F' ],
        [353, '630000', '青海省', '青', '632700', '玉树州', 'G' ],
        [354, '640000', '宁夏', '宁', '640100', '银川市', 'A' ],
        [355, '640000', '宁夏', '宁', '640200', '石嘴山市', 'B' ],
        [356, '640000', '宁夏', '宁', '640300', '吴忠市', 'C' ],
        [357, '640000', '宁夏', '宁', '640400', '固原市', 'D' ],
        [358, '640000', '宁夏', '宁', '640500', '中卫市', 'E' ],
        [359, '650000', '新疆', '新', '650200', '克拉玛依', 'J' ],
        [360, '650000', '新疆', '新', '', '乌鲁木齐市', 'A' ],
        [361, '650000', '新疆', '新', '', '奎屯', 'D' ],
        [362, '650000', '新疆', '新', '652100', '吐鲁番', 'K' ],
        [363, '650000', '新疆', '新', '652200', '哈密', 'L' ],
        [364, '650000', '新疆', '新', '652300', '昌吉', 'B' ],
        [365, '650000', '新疆', '新', '652700', '博尔塔拉', 'E' ],
        [366, '650000', '新疆', '新', '652800', '巴音郭楞', 'M' ],
        [367, '650000', '新疆', '新', '652900', '阿克苏', 'N' ],
        [368, '650000', '新疆', '新', '653000', '克孜勒苏', 'P' ],
        [369, '650000', '新疆', '新', '653100', '喀什', 'Q' ],
        [370, '650000', '新疆', '新', '653200', '和田', 'R' ],
        [371, '650000', '新疆', '新', '654000', '伊犁', 'F' ],
        [372, '650000', '新疆', '新', '654200', '塔城', 'G' ],
        [373, '650000', '新疆', '新', '654300', '阿勒泰', 'H' ],
        [374, '650000', '新疆', '新', '659001', '自治区直辖县级行政单位', 'C' ],
        [375, '310000', '上海市', '沪', '', '上海市', 'A' ],
        [376, '510000', '四川省', '川', '513400', '达州市', 'S' ],
        [377, '46000', '海南省', '琼', '', '三沙市', 'C' ],
        [378, '46000', '海南省', '琼', '', '文昌市', 'C' ],
        [379, '46000', '海南省', '琼', '', '万宁市', 'C' ],
        [380, '46000', '海南省', '琼', '', '定安县', 'C' ],
        [381, '46000', '海南省', '琼', '', '屯昌县', 'C' ],
        [382, '46000', '海南省', '琼', '', '澄迈县', 'C' ],
        [383, '46000', '海南省', '琼', '', '临高县', 'C' ],
        [384, '46000', '海南省', '琼', '', '东方市', 'D' ],
        [385, '46000', '海南省', '琼', '', '白沙县', 'D' ],
        [386, '46000', '海南省', '琼', '', '昌江县', 'D' ],
        [387, '46000', '海南省', '琼', '', '乐东县', 'D' ],
        [388, '46000', '海南省', '琼', '', '陵水县', 'D' ],
        [389, '46000', '海南省', '琼', '', '保亭县', 'D' ],
        [390, '46000', '海南省', '琼', '', '琼中县', 'D' ],
        [391, '46000', '海南省', '琼', '', '儋州市', 'F' ],
        ]
    str_sql='truncate table `grain_in_vehicleprovince`; '
    cursor=connection.cursor()
    cursor.execute(str_sql)
    cursor.close()
    connection.close()
    for ll in VLPLATE:
            defaultins=VehicleProvince.objects.create(code_id=str(ll[0]),province_id=ll[1],province_name=ll[2],province_code=ll[3],city_id=ll[4],city_name=ll[5],city_code=ll[6])
            defaultins.save()



# ################################
# 收购品种默认值


def acquisition_defaule():
    DEFAULT=[
        ['1','玉米',100000000000],
        ['2','水稻',100000000000],
        ['3','黄豆',100000000000],
    ]
    str_sql='truncate table `grain_in_acquisitionvarieties`; '
    cursor=connection.cursor()
    cursor.execute(str_sql)
    cursor.close()
    connection.close()
    for ll in DEFAULT:
            a=pypinyin.pinyin(ll[1],style=pypinyin.STYLE_FIRST_LETTER)
            b=[]
            for l1 in range(len(a)):
               b.append(str(a[l1][0]).title())
            c="".join(b)                  
            defaultins=AcquisitionVarieties.objects.create(AV_name=ll[1],find_code=ll[0],py_abbreviation=c,acquisitioncaps=ll[2])
            defaultins.save()


# 国标初始化

def GBforCorn():
      DEFAULT=[
          ['一等',1000,720,4.0,1,1,1,1,2.0,1,1,1,1.0,1,1,1,'正常','正常',14.0,1],
          ['二等',720,690,6.0,1,1,1,1,2.0,1,1,1,1.0,1,1,1,'正常','正常',14.0,1],
          ['三等',690,660,8.0,1,1,1,1,2.0,1,1,1,1.0,1,1,1,'正常','正常',14.0,1],
          ['四等',660,630,10.0,1,1,1,1,2.0,1,1,1,1.0,1,1,1,'正常','正常',14.0,1],
          ['五等',630,600,15.0,1,1,1,1,2.0,1,1,1,1.0,1,1,1,'正常','正常',14.0,1],
          ['等外',600,0,4.0,1,1,1,1,2.0,1,1,1,1.0,1,1,1,'正常','正常',14.0,1],
     ]
      sql_str='truncate table `grain_in_gbcorninformations`; '
      conn=connection.cursor()
      conn.execute(sql_str)      
      conn.close()
      connection.close()
      acquisition_name='玉米'
      file_name='GB 1353-2018玉米'
      fpath=os.path.join(settings.BASE_DIR,'GB1353-2018.pdf')
      with open(fpath,'rb') as ff:
            base64_str=base64.b64encode(ff.read())
            file_contents=base64_str.decode('utf-8')

      for ll in DEFAULT:
           conn=GBCornInformations.objects.create(acquisitionVarietiesid=acquisition_name,GB_filename=file_name,GB_file_contents=file_contents,purchase_price=0,purchase_name=ll[0],test_weight_high=ll[1],test_weight_low=ll[2])
           conn.save()



    
