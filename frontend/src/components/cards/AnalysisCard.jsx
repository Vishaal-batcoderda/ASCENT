import React from "react";
import ReactMarkdown from "react-markdown";
import GlassCard from "../ui/GlassCard";

function AnalysisCard({ analysis }) {
    if (!analysis) return null;

    return (
        <GlassCard>
            <h2 className="text-xl font-bold mb-4">Analysis Agent</h2>

            <div className="prose prose-invert max-w-none">
                <ReactMarkdown>{analysis}</ReactMarkdown>
            </div>
        </GlassCard>
    );
}

export default AnalysisCard;