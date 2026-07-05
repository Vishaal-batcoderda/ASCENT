import ReactMarkdown from "react-markdown";
import GlassCard from "../ui/GlassCard";

function ReportCard({ report }) {

    return (

        <GlassCard>

            <h2 className="text-xl font-semibold mb-5">
                AI Investment Report
            </h2>

            {
                report ? (

                    <article
                        className="
                            prose
                            prose-invert
                            max-w-none
                            prose-headings:mb-4
                            prose-headings:mt-6
                            prose-p:leading-8
                            prose-p:text-slate-300
                            prose-li:text-slate-300
                            prose-strong:text-white
                        "
                    >

                        <ReactMarkdown>
                            {report}
                        </ReactMarkdown>

                    </article>

                ) : (

                    <p className="text-slate-500">
                        Analyze a stock to generate an AI report.
                    </p>

                )

            }

        </GlassCard>

    );

}

export default ReportCard;