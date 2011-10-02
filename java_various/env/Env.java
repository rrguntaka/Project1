import java.io.*;
import java.util.*;

public class Env {
 public static Properties getEnvVars() throws Throwable {
  Process p = null;
  Properties envVars = new Properties();
  Runtime r = Runtime.getRuntime();
  String OS = System.getProperty("os.name").toLowerCase();
  //System.out.println(OS);

  p = r.exec( "cmd.exe /c set" );

  BufferedReader br = new BufferedReader
     ( new InputStreamReader( p.getInputStream() ) );
  String line;
  while( (line = br.readLine()) != null ) {
   int idx = line.indexOf( '=' );
   String key = line.substring( 0, idx );
   String value = line.substring( idx+1 );
   envVars.setProperty( key, value );
   // System.out.println( key + " = " + value );
   }
  return envVars;
  }

  public static void main(String args[]) {
   try {
     Properties p = ReadEnv.getEnvVars();
     String paths = p.getProperty("Path");
     String[] parray = paths.split(";");
     System.out.println(parray[0]);
     System.out.println(parray[1]);

     System.out.println("\n\nthe current value of Path is : \n\n" +
        p.getProperty("Path"));
     
     }
   catch (Throwable e) {
     e.printStackTrace();
     }
   }
  }