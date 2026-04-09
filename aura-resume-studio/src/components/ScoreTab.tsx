import React, { useEffect, useState } from "react";
import { motion } from "framer-motion";
import ScoreCard from "@/components/ScoreCard";
import { useApp } from "@/context/AppContext";
import { api } from "@/lib/api";

const ScoreTab: React.FC = () => {
  const { userType, resumeData, scoreData, setScoreData } = useApp();
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    if (resumeData && userType && !scoreData) {
      setLoading(true);
      api.scoreResume(resumeData.parsed_json, userType, resumeData.resume_id)
        .then(setScoreData)
        .catch(err => {
          console.error("Score failed:", err);
          alert("Failed to calculate score. API quota may be exceeded. Please try again later.");
        })
        .finally(() => setLoading(false));
    }
  }, [resumeData, userType, scoreData, setScoreData]);

  if (loading) {
    return (
      <div className="flex h-full items-center justify-center">
        <p className="text-sm text-muted-foreground animate-pulse">Calculating ATS score...</p>
      </div>
    );
  }

  if (!scoreData) {
    return (
      <div className="flex h-full items-center justify-center">
        <p className="text-sm text-muted-foreground">Upload a resume to see your score</p>
      </div>
    );
  }

  return (
    <div className="h-full overflow-y-auto p-4 space-y-6">
      {/* Overall Score */}
      <motion.div
        className="flex justify-center"
        initial={{ scale: 0.8, opacity: 0 }}
        animate={{ scale: 1, opacity: 1 }}
        transition={{ duration: 0.5 }}
      >
        <ScoreCard score={scoreData.overall_score} size={180} />
      </motion.div>

      {/* Parameter Breakdown */}
      <div className="space-y-3">
        <h3 className="text-sm font-semibold text-foreground">Score Breakdown</h3>
        {scoreData.parameters.map((p: any, i: number) => (
          <motion.div
            key={p.label}
            initial={{ opacity: 0, x: -16 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ delay: 0.1 * i }}
            className="space-y-1"
          >
            <div className="flex items-center justify-between">
              <span className="text-xs text-foreground">{p.label}</span>
              <div className="flex items-center gap-2">
                <span className="text-[10px] text-muted-foreground">{p.weight}%w</span>
                <span className="text-xs font-semibold text-foreground">{p.score}</span>
              </div>
            </div>
            <div className="h-1.5 w-full overflow-hidden rounded-full bg-secondary">
              <motion.div
                className="h-full rounded-full"
                style={{
                  background: p.score >= 80 ? "hsl(142 71% 45%)" : p.score >= 60 ? "hsl(45 93% 47%)" : "hsl(0 84% 60%)",
                }}
                initial={{ width: 0 }}
                animate={{ width: `${p.score}%` }}
                transition={{ delay: 0.2 + i * 0.08, duration: 0.6, ease: "easeOut" }}
              />
            </div>
            <p className="text-[10px] text-muted-foreground mt-1">{p.feedback}</p>
          </motion.div>
        ))}
      </div>
    </div>
  );
};

export default ScoreTab;
