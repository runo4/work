import java.util.*;

public class Food{
	public static void main(String[] args){
		Database db = new Database();
		
		db.setData("�L���E��", 50);
		db.setData("�i�X", 80);
		db.setData("�j���W��", 80);
		db.setData("�g�}�g", 100);
		db.setData("�J�{�`��", 250);
		
		Map<String, Integer> yasai = db.getData();
		
		int total = 0;
		for(String data : yasai.keySet()){
			System.out.println(data + " �̒l�i�� " + yasai.get(data) + " �~");
			total += yasai.get(data);
		}
		
		System.out.println("\n�����̍��v�z�� " + total + " �~�ł�");
	}
}
