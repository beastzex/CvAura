import React, { createContext, useContext, useState, useEffect } from "react";
import type { UserType } from "@/lib/mock-data";

interface ResumeData {
  session_id: string;
  resume_id: string;
  storage_url: string;
  parsed_json: any;
}

interface ScoreData {
  overall_score: number;
  parameters: any[];
}

interface AppState {
  userType: UserType | null;
  setUserType: (t: UserType) => void;
  uploaded: boolean;
  setUploaded: (v: boolean) => void;
  fileName: string;
  setFileName: (n: string) => void;
  isDark: boolean;
  toggleTheme: () => void;
  resumeData: ResumeData | null;
  setResumeData: (data: ResumeData) => void;
  scoreData: ScoreData | null;
  setScoreData: (data: ScoreData) => void;
}

const AppContext = createContext<AppState | null>(null);

export const useApp = () => {
  const ctx = useContext(AppContext);
  if (!ctx) throw new Error("useApp must be inside AppProvider");
  return ctx;
};

export const AppProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const [userType, setUserType] = useState<UserType | null>(null);
  const [uploaded, setUploaded] = useState(false);
  const [fileName, setFileName] = useState("");
  const [isDark, setIsDark] = useState(true);
  const [resumeData, setResumeData] = useState<ResumeData | null>(null);
  const [scoreData, setScoreData] = useState<ScoreData | null>(null);

  useEffect(() => {
    document.documentElement.classList.toggle("dark", isDark);
  }, [isDark]);

  const toggleTheme = () => setIsDark((p) => !p);

  return (
    <AppContext.Provider value={{ userType, setUserType, uploaded, setUploaded, fileName, setFileName, isDark, toggleTheme, resumeData, setResumeData, scoreData, setScoreData }}>
      {children}
    </AppContext.Provider>
  );
};
