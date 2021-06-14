import java.util.*;

public class Food{
	public static void main(String[] args){
		Database db = new Database();
		
		db.setData("キュウリ", 50);
		db.setData("ナス", 80);
		db.setData("ニンジン", 80);
		db.setData("トマト", 100);
		db.setData("カボチャ", 250);
		
		Map<String, Integer> yasai = db.getData();
		
		int total = 0;
		for(String data : yasai.keySet()){
			System.out.println(data + " の値段は " + yasai.get(data) + " 円");
			total += yasai.get(data);
		}
		
		System.out.println("\nそれらの合計額は " + total + " 円です");
	}
}
