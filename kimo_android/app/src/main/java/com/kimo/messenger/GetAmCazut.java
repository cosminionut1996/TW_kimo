package com.kimo.messenger;

import org.json.JSONException;
import org.json.JSONObject;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;

/**
 * Created by munte on 08.06.2017.
 */

public class GetAmCazut extends Messenger {

    String token;
    private static final String specificURL = "REST/accident/" +
            "";

    public GetAmCazut(String token) {
        this.token = token;
        this.requestURL = baseServerURL + specificURL + token;
    }

    @Override
    public JSONObject makeRequest() throws IOException, JSONException {
        URL url = new URL(requestURL);
        HttpURLConnection urlConnection = (HttpURLConnection) url.openConnection();
        urlConnection.setRequestMethod("GET");
        urlConnection.setRequestProperty("Content-Type", "application/json");
        urlConnection.setRequestProperty("charset", "utf-8");
        urlConnection.setUseCaches(false);
        urlConnection.setDoOutput(false);
        int res = urlConnection.getResponseCode();

        if (400 == res) {
            return new JSONObject("{error: 'Input criteria not correct'}");
        }
        if (422 == res) {
            return new JSONObject("{error: 'Invalid User'}");
        }
        if (500 == res) {
            return new JSONObject("{error: 'Internal server error'}");
        }
        if (503 == res) {
            return new JSONObject("{error: 'The server is currently unavailable'}");
        }
        if (200 == res) {
            BufferedReader br = new BufferedReader(new InputStreamReader(urlConnection.getInputStream(), "utf-8"));
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

