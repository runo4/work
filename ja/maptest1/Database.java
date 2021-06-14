import java.util.*;

public class Database{
	private Map<String, Integer> yasai;
	
	public Database(){
		yasai = new HashMap<>();
	}

	public void setData(String name, Integer price){
		yasai.put(name, price);
	}
	
	public Map<String, Integer> getData(){
		return yasai;
	}
}