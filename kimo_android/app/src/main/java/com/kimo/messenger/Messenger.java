package com.kimo.messenger;

/**
 * Created by munte on 29.05.2017.
 */

import org.json.JSONException;
import org.json.JSONObject;

import java.io.IOException;


public abstract class Messenger {

    private static final int port = 10001;
    private static final String host = "172.17.254.190"; //"192.168.0.103";
    private static final String version = "v1";
    private static final String urlPattern = "http://{host}:{port}/";

    protected String baseServerURL;
    protected String requestURL;


    public Messenger() {
        this.baseServerURL = urlPattern
                .replace("{host}", host)
                .replace("{port}", String.valueOf(port));
//                .replace("{version}", version);
    }

    String getHost() {
        return host;
    }

    String getVersion() {
        return version;
    }

    int getPort() {
        return port;
    }

    public abstract JSONObject makeRequest() throws IOException, JSONException;

    public String getRequestURL() {
        return requestURL;
    }

    public void setRequestURL(String requestURL) {
        this.requestURL = requestURL;
    }
}