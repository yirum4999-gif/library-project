package util;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class DBManager {
	
	private final static String URL = "jdbc:oracle:thin:@localhost:1521:xe";
	private final static String USER = "YOUREID";
	private final static String PASSWORD = "YOURPW";
	
	static{
		try {
			Class.forName("oracle.jdbc.driver.OracleDriver");
		} catch (ClassNotFoundException e) {
		e.printStackTrace();
		}
	}
	
	private static DBManager instance;
	public static DBManager getInctacne() {
		if (instance == null) {
			instance = new DBManager();
		}
		return instance;
	}
	
	private DBManager() {
	}
	
	public static Connection getConnection() throws SQLException {
        return DriverManager.getConnection(URL, USER, PASSWORD);
    }
}
