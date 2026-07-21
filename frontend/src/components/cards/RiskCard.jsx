import React from "react";
import GlassCard from "../ui/GlassCard";

function RiskCard({ risk }) {
    if (!risk) return null;

    return (
        <GlassCard>
            <h2 className="text-xl font-bold mb-4">
                Risk Agent
            </h2>

            <div className="space-y-4">

                <div>
                    <p className="text-sm opacity-70">
                        Risk Level
                    </p>

                    <p className="text-lg font-semibold">
                        {risk.level}
                    </p>
                </div>

                <div>
                    <p className="text-sm opacity-70">
                        Confidence
                    </p>

                    <p>
                        {risk.confidence}%
                    </p>
                </div>

                <div>
                    <p className="text-sm opacity-70">
                        Summary
                    </p>

                    <p>{risk.summary}</p>
                </div>

                {risk.factors?.length > 0 && (
                    <div>
                        <p className="text-sm opacity-70 mb-2">
                            Risk Factors
                        </p>

                        <ul className="list-disc pl-6">
                            {risk.factors.map((factor, index) => (
                                <li key={index}>{factor}</li>
                            ))}
                        </ul>
                    </div>
                )}

            </div>
        </GlassCard>
    );
}

export default RiskCard;