package com.chime.hack.server;



import java.io.IOException;

import org.jboss.resteasy.client.ClientRequest;
import org.jboss.resteasy.client.ClientResponse;




import com.chime.hack.client.GreetingService;
import com.chime.hack.shared.FieldVerifier;
import com.google.gwt.user.server.rpc.RemoteServiceServlet;



/**
 * The server-side implementation of the RPC service.
 */
@SuppressWarnings("serial")
public class GreetingServiceImpl extends RemoteServiceServlet implements
		GreetingService {

	public String greetServer(String input) throws Exception {
//		// Verify that the input is valid. 
//		if (!FieldVerifier.isValidName(input)) {
//			// If the input is not valid, throw an IllegalArgumentException back to
//			// the client.
//			throw new IllegalArgumentException(
//					"Name must be at least 4 characters long");
//		}
//
//		String serverInfo = getServletContext().getServerInfo();
//		String userAgent = getThreadLocalRequest().getHeader("User-Agent");
//
//		// Escape data from the client to avoid cross-site script vulnerabilities.
//		input = escapeHtml(input);
//		userAgent = escapeHtml(userAgent);
		
//		JSONResource resource = new Resty().json("http://192.168.56.102:8080/?age=35&gcsmotor=4&daysicu=10&normalscan=1");
//		try {
//			System.out.println(resource.object());
//			JSONObject obj = resource.object();
//		} catch (JSONException e) {
//			// TODO Auto-generated catch block
//			e.printStackTrace();
//		}
		String[] vars = input.split("\\|");
		ClientRequest req = new ClientRequest("http://192.168.56.102:8080/?age=" + vars[0] + "&gcsmotor=" + vars[2] + "&daysicu=" + vars[1] + "&normalscan="  + vars[3]);
        
 
        ClientResponse<String> res;
		
			res = req.get(String.class);
			
		
       

		return res.getEntity();
//		"Hello, " + input + "!<br><br>I am running " //+ serverInfo
//				+ ".<br><br>It looks like you are using:<br>";// + userAgent;
	}
	
	public void makeCall(){
		try {
			 
			
	 
		  } catch (Exception e) {
	 
			
		  }
	}

	/**
	 * Escape an html string. Escaping data received from the client helps to
	 * prevent cross-site script vulnerabilities.
	 * 
	 * @param html the html string to escape
	 * @return the escaped string
	 */
	private String escapeHtml(String html) {
		if (html == null) {
			return null;
		}
		return html.replaceAll("&", "&amp;").replaceAll("<", "&lt;")
				.replaceAll(">", "&gt;");
	}
}
