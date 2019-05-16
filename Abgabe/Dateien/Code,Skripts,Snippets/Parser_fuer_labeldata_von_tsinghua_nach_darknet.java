package parser;

import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Iterator;
import java.util.concurrent.atomic.AtomicBoolean;

import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;

public class Parser {

	static FileWriter nocyclist;
	static FileWriter parseexceptions;

	public static void main(String[] args) {
		JSONParser parser = new JSONParser();
		try {
			nocyclist = new FileWriter("/home/pacheco/data/eclipse-workspaces/java-playground/parser/nocyclist.txt");
			parseexceptions = new FileWriter(
					"/home/pacheco/data/eclipse-workspaces/java-playground/parser/parseexceptions.txt");
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
//		File f = new File(
//				"/home/pacheco/data/Master/bilddaten/cyclist_benchmark/labelData/test/tsinghuaDaimlerDataset");
//		work(f, parser);
//		f = new File("/home/pacheco/data/Master/bilddaten/cyclist_benchmark/labelData/train/tsinghuaDaimlerDataset");
//		work(f, parser);
//		f = new File("/home/pacheco/data/Master/bilddaten/cyclist_benchmark/labelData/valid/tsinghuaDaimlerDataset");
//		work(f, parser);
		
//		work("test",parser);
		work("train",parser);
//		work("valid",parser);

//		work("",parser);

		try {
			nocyclist.flush();
			nocyclist.close();
			parseexceptions.flush();
			parseexceptions.close();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

	private static void work(String str, JSONParser parser) {
		String labeldata = String
		.format("/home/pacheco/data/Master/bilddaten/benchmark/labelData/%s/tsinghuaDaimlerDataset", str);
		
//		labeldata="/home/pacheco/data/eclipse-workspaces/java-playground/parser";
		
		File f = new File(labeldata);
	
		File[] fileArray = f.listFiles();
		for (int i = 0; i < fileArray.length; i++) {
			if (fileArray[i].isDirectory()) {
				continue;
			}
			try {
				Object obj = parser.parse(new FileReader(fileArray[i]));
				String groundtruthfilename = fileArray[i].getAbsolutePath().replace(".json", ".txt")
						.replaceFirst("labelData", "labels").replace("labelData", "leftImg8bit");
				FileWriter file = new FileWriter(groundtruthfilename);
				JSONObject jsonObject = (JSONObject) obj;
//				System.out.println(jsonObject);
//				String name = (String) jsonObject.get("imagename");
//				System.out.println(name);
				JSONArray children = (JSONArray) jsonObject.get("children");
				@SuppressWarnings("unchecked")
				Iterator<JSONObject> iterator = children.iterator();
				AtomicBoolean firstline = new AtomicBoolean(true);
				while (iterator.hasNext()) {
					JSONObject child = iterator.next();
					String id = (String) child.get("identity");
					System.out.println(id+"\n"+i+"\n");
					if (!id.equals("cyclist")) {
						continue;
					}
					double dw = ((double) (1./2048));
					double dh = (double) (1./1024);
					double x = ((((long) child.get("mincol"))+((long) child.get("maxcol")))/2)-1;
					double y = ((((long) child.get("minrow"))+((long) child.get("maxrow")))/2)-1;
					double w = ((long) child.get("maxcol"))-((long) child.get("mincol"));
					double h = ((long) child.get("maxrow"))-((long) child.get("minrow"));
					x = (double) (x * dw);
					w = w * dw;
					y = y * dh;
					h = h * dh;

					
					
					
//					String x = Long.toString((Long) child.get("mincol"));
//					String width = Long.toString((Long) child.get("maxcol") - (Long) child.get("mincol"));
//					String y = Long.toString((Long) child.get("minrow"));
//					String height = Long.toString((Long) child.get("maxrow") - (Long) child.get("minrow"));
					file.write(firstline.get() ? String.format("0 %s %s %s %s",  x, y,w,h)
							: String.format("\n0 %s %s %s %s", x, y,w,h));
//					file.write(firstline.get() ? String.format("0 %s %s %s %s", Double.toString(x), Long.toString(y), Long.toString(w), Long.toString(h))
//							: String.format("\n0 %f %s %s %s", x, Long.toString(y), Long.toString(w), Long.toString(h)));
					firstline.set(false);
				}
				file.flush();
				file.close();
				if (firstline.get()) {
					nocyclist.write(fileArray[i].getAbsolutePath() + "\n");
					new File(groundtruthfilename).delete();
				}
			} catch (IOException e) {
				e.printStackTrace();
			} catch (ParseException e) {
				try {
					parseexceptions.write("Parse Exception in File " + fileArray[i].getAbsolutePath() + "\n");
				} catch (IOException e1) {
					// TODO Auto-generated catch block
					e1.printStackTrace();
				}
			}
		}
	}

}
