package com.kimo.messenger;

import com.kimo.messenger.Messenger;

import org.json.JSONException;
import org.json.JSONObject;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.net.HttpURLConnection;
import java.net.URL;

/**
 * Created by cschifirnet on 07-May-17.
 */

public class PostRequest extends Messenger {

    private static final String specificURL = "REST/token/";

    private Double latitudine;
    private Double longitudine;
    private String token;

    public PostRequest(double latitudine, double longitudine, String token) {
        this.latitudine = latitudine;
        this.longitudine = longitudine;
        this.token=token;
        this.requestURL = baseServerURL + specificURL + token;
    }

    @Override
    public JSONObject makeRequest() throws IOException, JSONException {
        URL url = new URL(requestURL);
        HttpURLConnection urlConn = (HttpURLConnection) url.openConnection();
        urlConn.setRequestProperty("Content-Type", "application/json");
        urlConn.setRequestProperty("charset", "utf-8");
        urlConn.setRequestMethod("PUT");
        urlConn.setUseCaches (false);
        urlConn.setDoOutput(true);
        OutputStreamWriter osw = new OutputStreamWriter(urlConn.getOutputStream());
        String to_send = "{\"longitudine\":" + this.longitudine.toString() + ", " +
                "\"latitudine\":" + this.latitudine.toString() + "}";
        osw.write(to_send);
        osw.flush();
        osw.close();

        int res = urlConn.getResponseCode();
        System.out.println("Res: " + res);

        if (400 == res) {
            return new JSONObject("{error: 'Data for creating new user is invalid'}");
        }
        if (500 == res) {
            return new JSONObject("{error: 'Internal server error'}");
        }
        if (503 == res) {
            return new JSONObject("{error: 'The server is currently unavailable'}");
        }
        if (201 == res) {
            BufferedReader br = new BufferedReader(new InputStreamReader(urlConn.getInputStream(), "utf-8"));
            StringBuilder sb = new StringBuilder();

            String line;
            while ((line = br.readLine()) != null) {
                sb.append(line).append("\n");
            }
            br.close();

            return new JSONObject(sb.toString());
        }
        return new JSONObject("{error: 'Unknown error'}");
    }
}
